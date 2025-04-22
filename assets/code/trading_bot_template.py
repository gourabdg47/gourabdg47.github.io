import requests
import time
import hashlib
import hmac
import json
from datetime import datetime, timedelta
import logging
from logging.handlers import TimedRotatingFileHandler
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod # Import for abstract base class

# --- Logging Configuration ---
# (Same as before - ensuring handlers aren't duplicated)
logger = logging.getLogger('TradingBot')
logger.setLevel(logging.INFO) # Set to DEBUG for more detail if needed
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
if not logger.handlers:
    log_filename = 'trading_bot_structured.log'
    file_handler = TimedRotatingFileHandler(log_filename, when='D', interval=1, backupCount=7)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.info(f"Logging initialized. Log file: {log_filename}")


# ==============================================================================
# Flexible Configuration Dictionary
# ==============================================================================
# --> MODIFY PARAMETERS HERE FOR STRATEGY TUNING <--
CONFIG = {
    # --- Bot Operation ---
    "LIVE_TRADING": False,             # <<< SET TO True FOR LIVE TRADING, False FOR BACKTESTING >>>
    "MAX_CONSECUTIVE_IDLE": 5,        # Warn after this many idle cycles
    "MIN_SLEEP_SECONDS": 10,          # Minimum time between cycles (live mode)

    # --- API & Connection ---
    "API_KEY": 'YOUR_API_KEY',         # Replace with your actual API Key (NEEDED FOR LIVE)
    "API_SECRET": 'YOUR_API_SECRET',   # Replace with your actual API Secret (NEEDED FOR LIVE)
    "BASE_URL": 'https://api.coindcx.com', # Adjust if needed
    "SYMBOL": 'XRPUSDT',
    "TIMEFRAME": '5m',                # e.g., '1m', '5m', '15m', '1h', '4h', '1d'
    "CONNECT_TIMEOUT": 10,            # Timeout for GET requests (seconds)
    "ORDER_TIMEOUT": 15,              # Timeout for POST requests (seconds)
    "OHLCV_LIMIT": 300,               # Number of candles to fetch (ensure enough for longest indicator)

    # --- Capital & Risk ---
    "INITIAL_CAPITAL": 100.0,         # Starting capital for calculations
    "LEVERAGE": 5,                    # REQUIRED, even for backtesting if strategy uses it for SL/TP/Sizing
    "RISK_PER_TRADE_PCT": 0.01,       # Risk 1% of current capital per trade (if using RISK_PCT_CAPITAL sizing)
    "POSITION_SIZING_METHOD": "RISK_PCT_CAPITAL", # Options: "RISK_PCT_CAPITAL", "FIXED_QTY", "ORIGINAL_LEVERAGED_RISK"
    "FIXED_TRADE_QTY": 10.0,          # Quantity in coins if using "FIXED_QTY" sizing

    # --- Stop Loss & Take Profit ---
    "SL_TP_METHOD": "ATR",            # Options: "PERCENT", "ATR", "SR_LEVEL"
    # - Percent Method -
    "STOP_LOSS_PCT": 0.01,            # Stop loss 1% price move (used if SL_TP_METHOD = "PERCENT")
    "TAKE_PROFIT_PCT": 0.02,          # Take profit 2% price move (used if SL_TP_METHOD = "PERCENT")
    # - ATR Method -
    "ATR_PERIOD": 14,                 # Period for ATR calculation
    "ATR_SL_MULTIPLIER": 1.5,         # Stop Loss = Entry +/- (ATR * Multiplier) / Leverage
    "ATR_TP_MULTIPLIER": 3.0,         # Take Profit = Entry +/- (ATR * Multiplier) / Leverage
    # - S/R Level Method (Requires SR calculation enabled in strategy) -
    "SR_TP_RR_RATIO": 2.0,            # Risk:Reward ratio if TP is not targeting next S/R

    # --- Default Strategy Specific Settings (Example) ---
    # These could be nested under a strategy-specific key if desired
    "USE_MA_CROSS": True,
    "FAST_MA_PERIOD": 9,
    "SLOW_MA_PERIOD": 21,

    "USE_RSI": True,
    "RSI_PERIOD": 14,
    "RSI_MID": 50,
    "RSI_OVERBOUGHT": 70,
    "RSI_OVERSOLD": 30,

    "USE_SR": True,                  # Use Support/Resistance levels
    "SR_PERIOD": 24,                 # Period for rolling min/max for S/R

    "USE_TREND_FILTER": False,         # Optional: Filter trades based on longer-term trend
    "TREND_FILTER_MA_PERIOD": 50,     # Period for the trend filter MA

    "SIGNAL_WEIGHTS": {               # Weights for DefaultMASRStrategy
        "MA_CROSS": 1,
        "RSI_CONFIRM": 1,
        "SR_BREAK": 1,
    },
    "BUY_SIGNAL_THRESHOLD": 2,        # Min positive strength for BUY (DefaultMASRStrategy)
    "SELL_SIGNAL_THRESHOLD": -2,      # Max negative strength for SELL (DefaultMASRStrategy)
}
# ==============================================================================

# --- Trading State Class ---
# (Remains largely the same as before, holds bot state)
class TradingState:
    def __init__(self, initial_capital):
        self.consecutive_idle = 0
        self.last_trade = None
        self.active_positions = [] # In live trading, holds info from get_open_positions
        self.idle_reasons = []
        self.current_capital = initial_capital # Track capital changes (more relevant for backtesting/simulation)
        self.trade_log = [] # Useful for backtesting results

    def log_state(self):
        # Adjust logging based on live/backtest context if needed
        logger.info(f"Current Capital (Simulated/Tracked): {self.current_capital:.2f} USDT")
        logger.info(f"Active Positions (Live Query): {len(self.active_positions)}")
        if self.last_trade:
            status = f"Last Trade: {self.last_trade.get('side','N/A').upper()} @ {self.last_trade.get('entry', 0):.5f} | Status: {self.last_trade.get('status', 'N/A')} | PnL: {self.last_trade.get('pnl', 'N/A')}"
            logger.info(status)

    def record_trade(self, trade_info):
        """Records trade details for analysis, especially useful for backtesting."""
        self.trade_log.append(trade_info)
        self.last_trade = trade_info # Keep track of the latest one

    # Methods to update capital, add/remove positions would be needed for accurate simulation/backtesting
    # For live trading, capital tracking often relies on exchange data primarily

# --- API Interaction Functions ---
# (get_signature, get_ohlcv, get_current_price, get_open_positions, place_order)
# These remain mostly the same but are now primarily used in LIVE mode.
# Backtesting will use historical data instead of live API calls for price/ohlcv.

def get_signature(secret, payload):
    payload_str = json.dumps(payload)
    return hmac.new(secret.encode('utf-8'), payload_str.encode('utf-8'), hashlib.sha256).hexdigest()

def get_ohlcv(config):
    """Fetches OHLCV data from the exchange. Used in LIVE mode."""
    try:
        endpoint = '/exchange/v1/derivatives/futures/data/candles'
        params = {'pair': config["SYMBOL"], 'interval': config["TIMEFRAME"], 'limit': config["OHLCV_LIMIT"]}
        url = config["BASE_URL"] + endpoint
        logger.debug(f"Fetching OHLCV from: {url} with params: {params}")
        response = requests.get(url, params=params, timeout=config["CONNECT_TIMEOUT"])
        response.raise_for_status()
        data = response.json()
        if not data:
            logger.warning("OHLCV data received is empty.")
            return None
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
        df = df.sort_values('timestamp').reset_index(drop=True)
        logger.debug(f"Successfully fetched {len(df)} OHLCV candles.")
        return df
    except requests.exceptions.RequestException as e:
        logger.error(f"OHLCV HTTP Error: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"OHLCV Processing Error: {str(e)}", exc_info=True)
        return None

def get_current_price(config):
    """Fetches the latest trade price from the exchange. Used in LIVE mode."""
    try:
        endpoint = '/exchange/v1/derivatives/futures/data/trades'
        params = {'pair': config["SYMBOL"], 'limit': 1}
        url = config["BASE_URL"] + endpoint
        response = requests.get(url, params=params, timeout=config["CONNECT_TIMEOUT"])
        response.raise_for_status()
        trades = response.json()
        if trades and 'price' in trades[0]:
            price = float(trades[0]['price'])
            logger.debug(f"Fetched current price: {price}")
            return price
        logger.warning(f"Could not fetch current price from trades endpoint for {config['SYMBOL']}. Response: {trades}")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Price Fetch HTTP Error: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Price Fetch Processing Error: {str(e)}", exc_info=True)
        return None

def get_open_positions(config):
    """Fetches real open positions from the exchange. Used in LIVE mode."""
    # --- VITAL: Replace with actual, authenticated API call for live trading ---
    if not config["LIVE_TRADING"]:
        logger.debug("Running in backtest mode - get_open_positions returning empty list.")
        return []

    logger.warning("SIMULATING get_open_positions: Returning empty list. NEEDS REAL API CALL FOR LIVE TRADING.")
    # Example structure (NEEDS IMPLEMENTATION):
    # try:
    #     endpoint = '/exchange/v1/derivatives/futures/positions'
    #     timestamp = int(time.time() * 1000)
    #     payload = {'timestamp': timestamp}
    #     signature = get_signature(config["API_SECRET"], payload)
    #     headers = {'X-AUTH-APIKEY': config["API_KEY"], 'X-AUTH-SIGNATURE': signature, 'Content-Type': 'application/json'}
    #     response = requests.post(config["BASE_URL"] + endpoint, json=payload, headers=headers, timeout=config["CONNECT_TIMEOUT"])
    #     response.raise_for_status()
    #     all_positions = response.json()
    #     symbol_positions = [pos for pos in all_positions if pos.get('pair') == config["SYMBOL"] and float(pos.get('quantity', 0)) != 0]
    #     logger.info(f"Fetched {len(symbol_positions)} open positions for {config['SYMBOL']}.")
    #     return symbol_positions
    # except Exception as e:
    #     logger.error(f"Failed to get open positions via API: {e}", exc_info=True)
    return [] # Return empty list on error or simulation

def place_order(config, side, quantity, order_type="MARKET", price=None, stop_loss=None, take_profit=None):
    """Places a real order on the exchange. Used in LIVE mode."""
    # --- VITAL: Replace with actual, authenticated API call for live trading ---
    if not config["LIVE_TRADING"]:
        logger.info(f"Backtest Mode: Simulating place_order {side} {quantity} {config['SYMBOL']}. SL={stop_loss} TP={take_profit}")
        # In a real backtester, this would just record the intended trade
        sim_order_id = f"backtest_{int(time.time())}_{side}"
        return {"status": "success", "order_id": sim_order_id, "message": "Simulated backtest order"}

    logger.warning(f"SIMULATING place_order: {side} {quantity:.4f} {config['SYMBOL']} SL={stop_loss:.5f} TP={take_profit:.5f}. NEEDS REAL API CALL FOR LIVE TRADING.")
    # Example structure (NEEDS IMPLEMENTATION):
    # try:
    #     # ... (Build payload as in original code) ...
    #     response = requests.post(config["BASE_URL"] + endpoint, json=full_payload, headers=headers, timeout=config["ORDER_TIMEOUT"])
    #     if response.status_code == 200 or response.status_code == 201: # Check Coindcx success codes
    #         logger.info(f"Live Order successfully placed via API. Response: {response.json()}")
    #         return response.json()
    #     else:
    #         logger.error(f"Live API Order Failed ({response.status_code}): {response.text}")
    #         return None
    # except Exception as e:
    #     logger.error(f"Live Order placement failed: {e}", exc_info=True)
    #     return None

    # --- Simulation Success Response for Live (if real API not implemented) ---
    sim_order_id = f"sim_live_{int(time.time())}_{side}"
    logger.info(f"Simulated live order success: {sim_order_id}")
    return {"status": "success", "order_id": sim_order_id, "message": "Simulated live order placed"}

# --- Indicator Calculation Functions ---
# (Moved some indicator logic into the Strategy class where appropriate)
# These can remain as helper functions or be part of a utility module.

def calculate_atr(df, period=14):
    if df is None or not all(col in df.columns for col in ['high', 'low', 'close']): return None
    if len(df) < period: return None
    high_low = df['high'] - df['low']
    high_close = np.abs(df['high'] - df['close'].shift())
    low_close = np.abs(df['low'] - df['close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.rolling(window=period, min_periods=period).mean() # Ensure full period
    return atr

def calculate_ma(series, period):
    if series is None or len(series) < period: return None
    return series.rolling(window=period, min_periods=period).mean()

def calculate_rsi(series, period=14):
    if series is None or len(series) < period + 1: return None # Need one extra for diff
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period, min_periods=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period, min_periods=period).mean()
    # Avoid division by zero
    if loss == 0: return pd.Series([100.0] * len(series)) # Or handle as appropriate
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_support_resistance(series, period):
    if series is None or len(series) < period: return None, None
    rolling_min = series.rolling(window=period, min_periods=period).min()
    rolling_max = series.rolling(window=period, min_periods=period).max()
    # Return the most recent S/R levels
    return (rolling_min.iloc[-1], rolling_max.iloc[-1])


# ==============================================================================
# Strategy Base Class (Template)
# ==============================================================================
class Strategy(ABC):
    """Abstract base class for all trading strategies."""
    def __init__(self, config):
        self.config = config
        self.name = "BaseStrategy" # Override in subclass

    @abstractmethod
    def calculate_indicators(self, df):
        """
        Calculate all necessary indicators for the strategy.
        Args:
            df (pd.DataFrame): DataFrame with OHLCV data.
        Returns:
            pd.DataFrame: DataFrame with calculated indicator columns added.
        """
        pass

    @abstractmethod
    def generate_signals(self, df_with_indicators, current_price):
        """
        Analyze indicators and generate buy/sell/hold signals.
        Args:
            df_with_indicators (pd.DataFrame): DataFrame with indicators.
            current_price (float): The current market price.
        Returns:
            dict: A dictionary containing analysis results and a 'signal' ('buy', 'sell', or None).
                  Example: {'conditions': {...}, 'analysis': {...}, 'signal': 'buy'}
        """
        pass

    @abstractmethod
    def calculate_sl_tp(self, side, entry_price, df_analysis):
        """
        Calculate Stop Loss and Take Profit levels based on the strategy.
        Args:
            side (str): 'buy' or 'sell'.
            entry_price (float): The trade entry price.
            df_analysis (dict): The output from generate_signals containing conditions/analysis.
        Returns:
            tuple: (stop_loss_price, take_profit_price)
        """
        pass

    @abstractmethod
    def calculate_position_size(self, current_price, state, stop_loss_price):
        """
        Calculate the position size for a new trade.
        Args:
            current_price (float): Current market price.
            state (TradingState): The current bot state (e.g., capital).
            stop_loss_price (float): Calculated stop loss price.
        Returns:
            float: Quantity of the asset to trade.
        """
        pass

# ==============================================================================
# Example Concrete Strategy Implementation (Refactored from original logic)
# ==============================================================================
class DefaultMASRStrategy(Strategy):
    """
    A strategy based on MA Crossover, RSI confirmation, and S/R breaks.
    Uses logic similar to the original script.
    """
    def __init__(self, config):
        super().__init__(config)
        self.name = "DefaultMA+SR"

    def calculate_indicators(self, df):
        """Calculates indicators specific to this strategy."""
        logger.debug(f"[{self.name}] Calculating indicators...")
        cfg = self.config # Shortcut

        if cfg["USE_MA_CROSS"]:
            df[f'fast_ma'] = calculate_ma(df['close'], cfg["FAST_MA_PERIOD"])
            df[f'slow_ma'] = calculate_ma(df['close'], cfg["SLOW_MA_PERIOD"])
            logger.debug(f"[{self.name}] Calculated MAs ({cfg['FAST_MA_PERIOD']}/{cfg['SLOW_MA_PERIOD']})")

        if cfg["USE_RSI"]:
            df[f'rsi'] = calculate_rsi(df['close'], cfg["RSI_PERIOD"])
            logger.debug(f"[{self.name}] Calculated RSI ({cfg['RSI_PERIOD']})")

        # ATR is needed for SL/TP calculation method "ATR" OR "SR_LEVEL" buffer OR potentially S/R logic
        if cfg["SL_TP_METHOD"] in ["ATR", "SR_LEVEL"] or cfg["USE_SR"]:
            df[f'atr'] = calculate_atr(df, cfg["ATR_PERIOD"])
            logger.debug(f"[{self.name}] Calculated ATR ({cfg['ATR_PERIOD']})")

        if cfg["USE_TREND_FILTER"]:
            df[f'trend_ma'] = calculate_ma(df['close'], cfg["TREND_FILTER_MA_PERIOD"])
            logger.debug(f"[{self.name}] Calculated Trend MA ({cfg['TREND_FILTER_MA_PERIOD']})")

        # Note: S/R calculation itself is done within generate_signals based on the latest data segment.
        # Adding it here would calculate it for the whole history unnecessarily unless needed for backtesting plots.
        logger.debug(f"[{self.name}] Indicator calculation complete.")
        return df

    def generate_signals(self, df_with_indicators, current_price):
        """Generates signals based on MA Cross, RSI, S/R, and Trend Filter."""
        if df_with_indicators is None or df_with_indicators.empty or current_price is None:
            logger.warning(f"[{self.name}] Insufficient data for signal generation.")
            return {'conditions': {}, 'analysis': {'signal_strength': 0}, 'signal': None}

        df = df_with_indicators # Use the df with pre-calculated indicators
        cfg = self.config
        latest_data = df.iloc[-1] # Use the latest row for signal logic trigger
        conditions = {}
        analysis = {'signal_strength': 0}
        signal = None # Default to no signal

        # --- Extract Latest Indicator Values ---
        fast_ma = latest_data.get('fast_ma')
        slow_ma = latest_data.get('slow_ma')
        rsi = latest_data.get('rsi')
        atr = latest_data.get('atr') # Needed for SL/TP calc later, store it
        trend_ma = latest_data.get('trend_ma')

        # Calculate latest S/R if needed (using the specified lookback period on the available history)
        support, resistance = None, None
        if cfg["USE_SR"]:
            sr_closes = df['close'].iloc[-cfg["SR_PERIOD"]:] # Use the last SR_PERIOD closes
            if len(sr_closes) >= cfg["SR_PERIOD"]:
                support = sr_closes.min()
                resistance = sr_closes.max()
                conditions['support'] = support
                conditions['resistance'] = resistance

        # --- Apply Logic & Calculate Signal Strength ---
        # 1. MA Cross
        if cfg["USE_MA_CROSS"] and fast_ma is not None and slow_ma is not None:
            # Check previous candle cross for entry signal trigger
            prev_fast_ma = df['fast_ma'].iloc[-2] if len(df) > 1 else None
            prev_slow_ma = df['slow_ma'].iloc[-2] if len(df) > 1 else None
            if prev_fast_ma is not None and prev_slow_ma is not None:
                if prev_fast_ma <= prev_slow_ma and fast_ma > slow_ma: # Bullish cross happened
                    conditions['ma_cross_signal'] = 'bullish'
                    analysis['signal_strength'] += cfg["SIGNAL_WEIGHTS"].get("MA_CROSS", 0)
                elif prev_fast_ma >= prev_slow_ma and fast_ma < slow_ma: # Bearish cross happened
                     conditions['ma_cross_signal'] = 'bearish'
                     analysis['signal_strength'] -= cfg["SIGNAL_WEIGHTS"].get("MA_CROSS", 0)
                else:
                    conditions['ma_cross_signal'] = 'none' # No cross this candle
            # Store current state for context
            conditions['ma_state'] = 'bullish' if fast_ma > slow_ma else 'bearish'
        else: conditions['ma_cross_signal'] = None; conditions['ma_state'] = None

        # 2. RSI Confirmation (based on current state)
        if cfg["USE_RSI"] and rsi is not None:
            conditions['rsi_state'] = 'bullish' if rsi > cfg["RSI_MID"] else 'bearish'
            if conditions.get('ma_state') == 'bullish' and conditions['rsi_state'] == 'bullish':
                 analysis['signal_strength'] += cfg["SIGNAL_WEIGHTS"].get("RSI_CONFIRM", 0)
            elif conditions.get('ma_state') == 'bearish' and conditions['rsi_state'] == 'bearish':
                 analysis['signal_strength'] -= cfg["SIGNAL_WEIGHTS"].get("RSI_CONFIRM", 0)
            conditions['rsi_value'] = rsi
        else: conditions['rsi_state'] = None

        # 3. S/R Break (check if price broke out recently)
        if cfg["USE_SR"] and support is not None and resistance is not None:
            prev_close = df['close'].iloc[-2] if len(df) > 1 else current_price # Use previous close
            if prev_close <= resistance and current_price > resistance:
                conditions['sr_break_signal'] = 'above_resistance'
                analysis['signal_strength'] += cfg["SIGNAL_WEIGHTS"].get("SR_BREAK", 0)
            elif prev_close >= support and current_price < support:
                conditions['sr_break_signal'] = 'below_support'
                analysis['signal_strength'] -= cfg["SIGNAL_WEIGHTS"].get("SR_BREAK", 0)
            else:
                conditions['sr_break_signal'] = 'none'
            conditions['sr_state'] = 'within_range' if support < current_price < resistance else 'outside_range'
        else: conditions['sr_break_signal'] = None; conditions['sr_state'] = None

        # 4. Trend Filter (Acts as a gate)
        conditions['trend_filter_allow'] = True # Default to allow
        if cfg["USE_TREND_FILTER"] and trend_ma is not None:
            if current_price > trend_ma: conditions['trend_filter_direction'] = 'bullish'
            elif current_price < trend_ma: conditions['trend_filter_direction'] = 'bearish'
            else: conditions['trend_filter_direction'] = 'neutral'

            # Only allow trades in direction of trend filter IF a signal is potentially generated
            if analysis['signal_strength'] > 0 and conditions['trend_filter_direction'] == 'bearish':
                conditions['trend_filter_allow'] = False
            if analysis['signal_strength'] < 0 and conditions['trend_filter_direction'] == 'bullish':
                conditions['trend_filter_allow'] = False
        else: conditions['trend_filter_direction'] = None


        # --- Determine Final Signal ---
        if conditions['trend_filter_allow']:
            if analysis['signal_strength'] >= cfg["BUY_SIGNAL_THRESHOLD"]:
                signal = 'buy'
            elif analysis['signal_strength'] <= cfg["SELL_SIGNAL_THRESHOLD"]:
                signal = 'sell'

        # --- Log Analysis Summary ---
        log_msg = f"[{self.name}] Analysis @ {current_price:.5f}: Strength={analysis['signal_strength']}"
        if conditions.get('ma_cross_signal') != 'none': log_msg += f" | MA Signal: {conditions['ma_cross_signal']}"
        if conditions.get('rsi_state'): log_msg += f" | RSI State: {conditions['rsi_state']} ({conditions.get('rsi_value', 0):.1f})"
        if conditions.get('sr_break_signal') != 'none': log_msg += f" | SR Signal: {conditions['sr_break_signal']}"
        if cfg["USE_TREND_FILTER"]: log_msg += f" | Trend ({cfg['TREND_FILTER_MA_PERIOD']}MA): {conditions.get('trend_filter_direction','N/A')} (Allow: {conditions['trend_filter_allow']})"
        log_msg += f" | FINAL SIGNAL: {signal}"
        logger.info(log_msg)

        # Store latest indicator values used, including ATR needed for SL/TP calc
        conditions['fast_ma'] = fast_ma
        conditions['slow_ma'] = slow_ma
        conditions['atr'] = atr # Pass ATR through

        return {'conditions': conditions, 'analysis': analysis, 'signal': signal}

    def calculate_sl_tp(self, side, entry_price, df_analysis):
        """Calculates SL/TP based on configured method (PERCENT, ATR, SR_LEVEL)."""
        cfg = self.config
        method = cfg["SL_TP_METHOD"]
        conditions = df_analysis.get('conditions', {})
        atr = conditions.get('atr') # Get ATR from analysis if available
        support = conditions.get('support')
        resistance = conditions.get('resistance')
        leverage = cfg["LEVERAGE"] # Leverage affects the price distance required for SL/TP %

        stop_loss, take_profit = None, None
        logger.debug(f"[{self.name}] Calculating SL/TP using method: {method}")

        if method == "PERCENT":
            if leverage <= 0:
                logger.error("Leverage must be positive for PERCENT SL/TP calculation.")
                return None, None
            if side == 'buy':
                stop_loss = entry_price * (1 - cfg["STOP_LOSS_PCT"] / leverage)
                take_profit = entry_price * (1 + cfg["TAKE_PROFIT_PCT"] / leverage)
            else: # sell
                stop_loss = entry_price * (1 + cfg["STOP_LOSS_PCT"] / leverage)
                take_profit = entry_price * (1 - cfg["TAKE_PROFIT_PCT"] / leverage)
            logger.info(f"[{self.name}] SL/TP (Percent): SL={stop_loss:.5f}, TP={take_profit:.5f}")

        elif method == "ATR":
            if atr is None or atr <= 0:
                logger.error(f"[{self.name}] Cannot use ATR method: ATR is not calculated or invalid ({atr}).")
                return None, None
            if leverage <= 0:
                 logger.error("Leverage must be positive for ATR SL/TP calculation.")
                 return None, None
            atr_adj = atr / leverage # Adjust ATR value based on leverage for price distance
            if side == 'buy':
                stop_loss = entry_price - (atr_adj * cfg["ATR_SL_MULTIPLIER"])
                take_profit = entry_price + (atr_adj * cfg["ATR_TP_MULTIPLIER"])
            else: # sell
                stop_loss = entry_price + (atr_adj * cfg["ATR_SL_MULTIPLIER"])
                take_profit = entry_price - (atr_adj * cfg["ATR_TP_MULTIPLIER"])
            logger.info(f"[{self.name}] SL/TP (ATR={atr:.5f}, LvgAdjATR={atr_adj:.5f}): SL={stop_loss:.5f}, TP={take_profit:.5f}")

        elif method == "SR_LEVEL":
            if support is None or resistance is None:
                logger.error(f"[{self.name}] Cannot use S/R method: Support/Resistance not available in analysis.")
                return None, None
            # Use ATR for buffer if available, otherwise fallback to a small percentage?
            sl_buffer = (atr * 0.5 / leverage) if (atr and atr > 0 and leverage > 0) else (entry_price * 0.001 / leverage) # Example buffer logic
            sl_buffer = max(sl_buffer, 0.00001) # Ensure buffer is non-zero

            if side == 'buy':
                stop_loss = support - sl_buffer
                risk_amount = entry_price - stop_loss
                if risk_amount <= 0: logger.warning(f"[{self.name}] Calculated risk is zero or negative in SR SL/TP. Check S/R levels."); risk_amount = entry_price * cfg["STOP_LOSS_PCT"] / leverage # Fallback risk
                take_profit = entry_price + (risk_amount * cfg["SR_TP_RR_RATIO"])
                # Optional: Cap TP near resistance? take_profit = min(take_profit, resistance - sl_buffer)
            else: # sell
                stop_loss = resistance + sl_buffer
                risk_amount = stop_loss - entry_price
                if risk_amount <= 0: logger.warning(f"[{self.name}] Calculated risk is zero or negative in SR SL/TP. Check S/R levels."); risk_amount = entry_price * cfg["STOP_LOSS_PCT"] / leverage # Fallback risk
                take_profit = entry_price - (risk_amount * cfg["SR_TP_RR_RATIO"])
                # Optional: Cap TP near support? take_profit = max(take_profit, support + sl_buffer)
            logger.info(f"[{self.name}] SL/TP (S/R S:{support:.5f} R:{resistance:.5f} Buf:{sl_buffer:.5f}): SL={stop_loss:.5f}, TP={take_profit:.5f}")

        else:
            logger.error(f"[{self.name}] Unknown SL/TP method: {method}")
            return None, None

        # Basic validation
        if side == 'buy' and stop_loss is not None and take_profit is not None and (stop_loss >= entry_price or take_profit <= entry_price):
            logger.error(f"[{self.name}] Invalid Buy SL/TP: Entry={entry_price:.5f}, SL={stop_loss:.5f}, TP={take_profit:.5f}")
            return None, None
        if side == 'sell' and stop_loss is not None and take_profit is not None and (stop_loss <= entry_price or take_profit >= entry_price):
            logger.error(f"[{self.name}] Invalid Sell SL/TP: Entry={entry_price:.5f}, SL={stop_loss:.5f}, TP={take_profit:.5f}")
            return None, None

        return stop_loss, take_profit

    def calculate_position_size(self, current_price, state, stop_loss_price):
        """Calculates position size based on configured method."""
        cfg = self.config
        method = cfg["POSITION_SIZING_METHOD"]
        qty = 0.0

        if stop_loss_price is None:
            logger.error(f"[{self.name}] Cannot calculate position size: Stop loss price is None.")
            return 0.0
        if current_price == stop_loss_price:
             logger.error(f"[{self.name}] Cannot calculate position size: Entry price {current_price} is equal to Stop loss price {stop_loss_price}.")
             return 0.0

        price_difference = abs(current_price - stop_loss_price)
        if price_difference <= 0: # Use a small epsilon for floating point check?
             logger.error(f"[{self.name}] Cannot calculate position size: Zero or negative price difference for stop loss ({price_difference}).")
             return 0.0

        if method == "RISK_PCT_CAPITAL":
            capital_to_risk = state.current_capital * cfg["RISK_PER_TRADE_PCT"]
            # Qty = Amount willing to risk / Risk per unit of asset
            # Risk per unit = Price difference between entry and stop loss
            qty = capital_to_risk / price_difference
            logger.info(f"[{self.name}] Sizing (Risk % Cap): Risking {capital_to_risk:.2f} USDT ({cfg['RISK_PER_TRADE_PCT']*100}%), SL Diff: {price_difference:.5f}, Qty: {qty:.4f}")

        elif method == "FIXED_QTY":
            qty = cfg["FIXED_TRADE_QTY"]
            logger.info(f"[{self.name}] Sizing (Fixed Qty): Using fixed quantity {qty:.4f}")

        elif method == "ORIGINAL_LEVERAGED_RISK":
            # This interpretation might need refinement based on exact definition needed
            capital_to_risk = cfg["INITIAL_CAPITAL"] * cfg["RISK_PER_TRADE_PCT"] # Based on INITIAL capital
            # Assumes STOP_LOSS_PCT defines the risk relative to entry, adjusted by leverage
            if cfg["STOP_LOSS_PCT"] <= 0 or cfg["LEVERAGE"] <=0:
                 logger.error(f"[{self.name}] ORIGINAL_LEVERAGED_RISK requires STOP_LOSS_PCT and LEVERAGE > 0 in config.")
                 return 0.0
            stop_loss_distance_pct_of_entry = cfg["STOP_LOSS_PCT"] / cfg["LEVERAGE"]
            risk_per_coin = current_price * stop_loss_distance_pct_of_entry
            if risk_per_coin <= 0:
                 logger.error(f"[{self.name}] Calculated risk per coin is zero or negative in ORIGINAL method.")
                 return 0.0
            qty = capital_to_risk / risk_per_coin
            logger.warning(f"[{self.name}] Sizing (Original Leveraged Risk - USE WITH CAUTION): Risking {capital_to_risk:.2f} USDT based on Initial Cap. SLDist%={stop_loss_distance_pct_of_entry*100:.2f}%. Qty: {qty:.4f}")

        else:
            logger.error(f"[{self.name}] Unknown position sizing method: {method}")
            return 0.0

        # Add exchange minimum order size checks here if known (e.g., min qty for XRPUSDT)
        min_order_qty = 0.01 # Example: Check actual exchange minimums
        if qty < min_order_qty:
            logger.error(f"[{self.name}] Calculated quantity {qty:.4f} is below minimum order size {min_order_qty}.")
            return 0.0
        if qty <= 0:
            logger.error(f"[{self.name}] Calculated quantity is zero or negative ({qty}). Check config and prices.")
            return 0.0

        # Optional: Add max position size constraints

        return qty

# --- Helper function for idle reasons ---
def log_idle_reason(strategy_name, analysis_result, config):
    """Logs reasons why no trade signal was generated."""
    reasons = []
    conditions = analysis_result.get('conditions', {})
    analysis = analysis_result.get('analysis', {})
    strength = analysis.get('signal_strength', 0)
    signal = analysis_result.get('signal') # Get the final signal determination

    if signal is None: # Only log reasons if no final signal
        if not conditions.get('trend_filter_allow', True):
            reasons.append(f"Trend filter block ({conditions.get('trend_filter_direction')})")
        elif strength < config["BUY_SIGNAL_THRESHOLD"] and strength > config["SELL_SIGNAL_THRESHOLD"]:
             # Be more specific based on strategy logic if possible
             if conditions.get('ma_cross_signal') == 'none' and conditions.get('sr_break_signal') == 'none':
                  reasons.append("No primary signal (MA cross or SR break)")
             else:
                  reasons.append(f"Signal strength ({strength}) within neutral zone ({config['SELL_SIGNAL_THRESHOLD']} to {config['BUY_SIGNAL_THRESHOLD']})")
        else:
            # If strength was outside neutral but still no signal (e.g., trend filter)
             if not conditions.get('trend_filter_allow', True):
                 reasons.append(f"Signal ({'buy' if strength > 0 else 'sell'}) generated but blocked by trend filter.")
             else:
                 reasons.append("Conditions not met (check detailed logs/strategy logic)") # Generic fallback

    if not reasons: reasons.append("No trade signal generated by strategy") # Default if no other reason found
    logger.info(f"[{strategy_name}] Idle cycle. Reasons: {'; '.join(reasons)}")
    return reasons


# --- Timing Function ---
def calculate_next_run_delay(config):
    """Calculates sleep time until the start of the next candle."""
    now = datetime.now()
    tf_unit = ''.join(filter(str.isalpha, config["TIMEFRAME"])).lower()
    tf_value = int(''.join(filter(str.isdigit, config["TIMEFRAME"])))

    if tf_value <= 0: tf_value = 1 # Safety net

    next_run = None
    current_second = now.second
    current_microsecond = now.microsecond

    try:
        if tf_unit == 'm':
            minutes_past_hour = now.minute
            next_run_minute = ((minutes_past_hour // tf_value) + 1) * tf_value
            delta_minutes = next_run_minute - minutes_past_hour
            if delta_minutes == 0: # If exactly on the minute, wait for next interval
                 delta_minutes = tf_value
            next_run = now.replace(second=0, microsecond=0) + timedelta(minutes=delta_minutes)

        elif tf_unit == 'h':
            hours_past_day = now.hour
            next_run_hour = ((hours_past_day // tf_value) + 1) * tf_value
            delta_hours = next_run_hour - hours_past_day
            if delta_hours == 0:
                 delta_hours = tf_value
            # Check if next run hour exceeds 23 (roll over day)
            if next_run_hour >= 24:
                next_run = (now + timedelta(days=1)).replace(hour=next_run_hour % 24, minute=0, second=0, microsecond=0)
            else:
                 next_run = now.replace(hour=next_run_hour, minute=0, second=0, microsecond=0)

        elif tf_unit == 'd':
             # This needs more careful handling of days if tf_value > 1
             if tf_value == 1:
                 next_run = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
             else:
                 # Logic for multi-day timeframes (more complex)
                 logger.warning(f"Multi-day timeframe ({config['TIMEFRAME']}) timing might be imprecise.")
                 next_run = (now + timedelta(days=tf_value)).replace(hour=0, minute=0, second=0, microsecond=0) # Approximate
        else:
            logger.error(f"Unsupported timeframe unit: {tf_unit}. Defaulting to 1 minute delay.")
            return 60.0

        sleep_time = (next_run - now).total_seconds()

        # Add a small buffer (e.g., 1 second) to ensure the candle is closed
        buffer = 1.0
        sleep_time += buffer

    except Exception as e:
         logger.error(f"Error calculating next run time: {e}. Defaulting to 60s delay.", exc_info=True)
         return 60.0

    # Ensure minimum sleep time
    return max(sleep_time, config["MIN_SLEEP_SECONDS"])


# --- Main Bot Loop (Live Trading) ---
def run_live_bot(config, strategy):
    """Main loop for live trading."""
    state = TradingState(config["INITIAL_CAPITAL"])
    logger.info(f"===== Starting LIVE {config['SYMBOL']} Futures Bot ({strategy.name}) =====")
    logger.info(f"Strategy Config: TF={config['TIMEFRAME']}, Leverage={config['LEVERAGE']}")
    logger.info(f"Risk: SizeMethod={config['POSITION_SIZING_METHOD']}, SL/TP Method={config['SL_TP_METHOD']}")
    logger.info("--------------------------------------------------")

    while True:
        try:
            # --- Wait for next candle ---
            sleep_time = calculate_next_run_delay(config)
            logger.info(f"Next execution approx: {(datetime.now() + timedelta(seconds=sleep_time)).strftime('%Y-%m-%d %H:%M:%S')} (sleeping {sleep_time:.1f}s)")
            time.sleep(sleep_time)

            logger.info("--- Cycle Start ---")
            # --- Fetch Data & Analyze ---
            df_ohlcv_raw = get_ohlcv(config)
            if df_ohlcv_raw is None or df_ohlcv_raw.empty:
                logger.warning("Failed to get OHLCV data, skipping cycle.")
                time.sleep(30) # Wait longer if data fetch fails
                continue

            # Calculate indicators using the strategy
            df_with_indicators = strategy.calculate_indicators(df_ohlcv_raw.copy()) # Pass a copy

            # Get current price *after* indicator calculation (closer to execution time)
            current_price = get_current_price(config)
            if current_price is None:
                logger.warning("Failed to get current price, using last close price for analysis.")
                current_price = df_with_indicators['close'].iloc[-1] if not df_with_indicators.empty else None
                if current_price is None:
                     logger.error("Cannot proceed without a valid current price.")
                     time.sleep(30)
                     continue

            # Generate signals using the strategy
            analysis_result = strategy.generate_signals(df_with_indicators, current_price)
            signal = analysis_result.get('signal')

            # --- Check Existing Positions (CRITICAL FOR LIVE) ---
            state.active_positions = get_open_positions(config) # MUST BE REAL API CALL
            state.log_state() # Log capital and position status

            if state.active_positions:
                logger.info(f"Active position(s) detected ({len(state.active_positions)}) - Skipping new signal check.")
                # Optional: Add logic here to manage existing positions (e.g., trailing stops based on strategy)
                state.consecutive_idle = 0
                state.idle_reasons = []
                continue # Skip to next cycle if already in a position

            # --- Execute Trade ---
            if signal:
                logger.info(f"[{strategy.name}] Trade Signal: {signal.upper()}")
                # 1. Calculate SL/TP levels using strategy
                stop_loss_price, take_profit_price = strategy.calculate_sl_tp(signal, current_price, analysis_result)
                if stop_loss_price is None or take_profit_price is None:
                    logger.error(f"[{strategy.name}] Failed to calculate valid SL/TP levels. Cannot place order.")
                    continue # Skip trade

                # 2. Calculate Position Size using strategy
                position_size_coins = strategy.calculate_position_size(current_price, state, stop_loss_price)
                if position_size_coins <= 0:
                     logger.error(f"[{strategy.name}] Failed to calculate valid position size ({position_size_coins}). Cannot place order.")
                     continue # Skip trade

                # 3. Place Order (NEEDS REAL API CALL via place_order function)
                logger.info(f"[{strategy.name}] Attempting to place LIVE {signal.upper()} order: Qty={position_size_coins:.4f}, Entry~={current_price:.5f}, SL={stop_loss_price:.5f}, TP={take_profit_price:.5f}")
                order_result = place_order(
                    config=config,
                    side=signal,
                    quantity=position_size_coins,
                    stop_loss=stop_loss_price,
                    take_profit=take_profit_price
                )

                # 4. Update State (Based on API Response)
                if order_result and order_result.get("status") == "success": # Adjust check based on REAL API response
                    logger.info(f"[{strategy.name}] LIVE Order placement successful (Simulated/API). ID: {order_result.get('order_id', 'N/A')}")
                    trade_info = {
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'side': signal,
                        'entry': current_price, # Actual entry might differ slightly
                        'sl': stop_loss_price,
                        'tp': take_profit_price,
                        'qty': position_size_coins,
                        'order_id': order_result.get('order_id'),
                        'status': 'open', # Assume open until confirmed closed/filled
                        'pnl': 'N/A'
                    }
                    state.record_trade(trade_info)
                    # In a real bot, you'd start monitoring this order_id
                    state.consecutive_idle = 0
                    state.idle_reasons = []
                    # LIVE capital updates should ideally come from exchange balance checks
                else:
                    logger.error(f"[{strategy.name}] LIVE Order placement failed. API Response: {order_result}")
                    # Potentially add retry logic or cooldown

            else: # No signal
                reasons = log_idle_reason(strategy.name, analysis_result, config)
                state.idle_reasons.extend(reasons)
                state.consecutive_idle += 1

                if state.consecutive_idle >= config["MAX_CONSECUTIVE_IDLE"] and state.consecutive_idle % config["MAX_CONSECUTIVE_IDLE"] == 0:
                    logger.warning(f"Bot has been idle for {state.consecutive_idle} cycles.")
                    unique_reasons = sorted(list(set(state.idle_reasons[-(state.consecutive_idle * 2):]))) # Look at recent reasons
                    logger.warning(f"[{strategy.name}] Recent unique idle reasons:\n- " + "\n- ".join(unique_reasons))

            logger.info("--- Cycle End ---")

        except KeyboardInterrupt:
            logger.info("Keyboard interrupt received. Shutting down live bot.")
            break
        except Exception as e:
            logger.error(f"!!! Unhandled error in LIVE main loop: {str(e)} !!!", exc_info=True)
            logger.info("Waiting 60 seconds before next cycle after error...")
            time.sleep(60)

# ==============================================================================
# Backtester Class (Placeholder)
# ==============================================================================
class Backtester:
    def __init__(self, config, strategy):
        self.config = config
        self.strategy = strategy
        self.state = TradingState(config["INITIAL_CAPITAL"])
        logger.info(f"===== Initializing Backtester for {config['SYMBOL']} ({strategy.name}) =====")

    def load_historical_data(self):
        """
        Placeholder for loading historical data.
        Should load data based on config (e.g., symbol, timeframe, date range).
        Returns:
            pd.DataFrame: DataFrame with historical OHLCV data.
                          Columns: ['timestamp', 'open', 'high', 'low', 'close', 'volume']
                          Timestamp should be datetime objects, sorted ascending.
        """
        logger.warning("Backtester.load_historical_data() needs implementation.")
        logger.warning("Returning dummy data for structure demonstration.")
        # --- Replace with actual data loading (e.g., from CSV, database, API history endpoint) ---
        # Example: Fetch limited data using get_ohlcv for structure demo (NOT suitable for real backtest)
        dummy_df = get_ohlcv({**self.config, "OHLCV_LIMIT": 500}) # Fetch more for demo
        if dummy_df is None:
             logger.error("Failed to load even dummy historical data.")
             return pd.DataFrame()
        logger.info(f"Loaded {len(dummy_df)} (dummy) historical data points for backtest.")
        return dummy_df


    def run(self):
        """Runs the backtest simulation loop."""
        logger.info("--- Starting Backtest Run ---")
        historical_data = self.load_historical_data()

        if historical_data.empty:
            logger.error("No historical data loaded. Aborting backtest.")
            return None

        # Calculate indicators on the entire dataset first
        logger.info("Calculating indicators for historical data...")
        df_with_indicators = self.strategy.calculate_indicators(historical_data.copy())

        logger.info("Starting simulation loop over historical data...")
        active_trade = None # Track the currently open simulated trade

        # Loop through each candle in the historical data
        for i in range(1, len(df_with_indicators)): # Start from 1 to have previous candle data
            current_candle = df_with_indicators.iloc[i]
            # Use a slice of the dataframe up to the current point for signal generation context
            current_df_slice = df_with_indicators.iloc[:i+1]
            # Simulate 'current_price' - typically use the open or close of the *current* candle for decisions
            sim_current_price = current_candle['open'] # Simulate decision at candle open

            # --- Check for SL/TP Hits on Active Trade ---
            if active_trade:
                hit_sl_tp = False
                pnl = 0
                # Check SL
                if active_trade['side'] == 'buy' and current_candle['low'] <= active_trade['sl']:
                    exit_price = active_trade['sl']
                    active_trade['status'] = 'closed_sl'
                    hit_sl_tp = True
                    logger.info(f"Backtest: LONG SL hit @ {exit_price:.5f} (Low: {current_candle['low']:.5f})")
                elif active_trade['side'] == 'sell' and current_candle['high'] >= active_trade['sl']:
                     exit_price = active_trade['sl']
                     active_trade['status'] = 'closed_sl'
                     hit_sl_tp = True
                     logger.info(f"Backtest: SHORT SL hit @ {exit_price:.5f} (High: {current_candle['high']:.5f})")
                # Check TP
                elif active_trade['side'] == 'buy' and current_candle['high'] >= active_trade['tp']:
                     exit_price = active_trade['tp']
                     active_trade['status'] = 'closed_tp'
                     hit_sl_tp = True
                     logger.info(f"Backtest: LONG TP hit @ {exit_price:.5f} (High: {current_candle['high']:.5f})")
                elif active_trade['side'] == 'sell' and current_candle['low'] <= active_trade['tp']:
                     exit_price = active_trade['tp']
                     active_trade['status'] = 'closed_tp'
                     hit_sl_tp = True
                     logger.info(f"Backtest: SHORT TP hit @ {exit_price:.5f} (Low: {current_candle['low']:.5f})")

                if hit_sl_tp:
                    # Calculate PnL (simplified - ignores fees/slippage)
                    price_diff = exit_price - active_trade['entry']
                    if active_trade['side'] == 'sell': price_diff = -price_diff
                    pnl = price_diff * active_trade['qty'] # Simple PnL in quote currency
                    active_trade['pnl'] = pnl
                    active_trade['exit_price'] = exit_price
                    active_trade['exit_timestamp'] = current_candle['timestamp']
                    self.state.current_capital += pnl # Update capital
                    self.state.record_trade(active_trade.copy()) # Log the closed trade
                    logger.info(f"Backtest: Trade Closed. PnL: {pnl:.2f} USDT. New Capital: {self.state.current_capital:.2f} USDT")
                    active_trade = None


            # --- Check for New Signals (only if no active trade) ---
            if not active_trade:
                # Generate signals using the strategy based on data *up to the previous candle*
                # or use current open for decision logic, depends on strategy design
                analysis_result = self.strategy.generate_signals(current_df_slice, sim_current_price)
                signal = analysis_result.get('signal')

                if signal:
                    logger.info(f"Backtest: Signal {signal.upper()} @ {sim_current_price:.5f} on {current_candle['timestamp']}")
                    # 1. Calculate SL/TP
                    sl, tp = self.strategy.calculate_sl_tp(signal, sim_current_price, analysis_result)
                    if sl is None or tp is None:
                        logger.warning("Backtest: Invalid SL/TP calculated, skipping signal.")
                        continue

                    # 2. Calculate Position Size
                    qty = self.strategy.calculate_position_size(sim_current_price, self.state, sl)
                    if qty <= 0:
                         logger.warning(f"Backtest: Invalid position size ({qty}), skipping signal.")
                         continue

                    # 3. Simulate Order Placement -> Create active_trade
                    active_trade = {
                        'timestamp': current_candle['timestamp'],
                        'side': signal,
                        'entry': sim_current_price, # Assume entry at open
                        'sl': sl,
                        'tp': tp,
                        'qty': qty,
                        'order_id': f"bt_{i}",
                        'status': 'open',
                        'pnl': 'N/A' # PnL calculated on close
                    }
                    logger.info(f"Backtest: Entered {signal.upper()} | Qty: {qty:.4f} | Entry: {sim_current_price:.5f} | SL: {sl:.5f} | TP: {tp:.5f}")

            # Optional: Log state periodically during backtest
            if i % 100 == 0: # Log every 100 candles
                 logger.debug(f"Backtest progress: Candle {i}/{len(df_with_indicators)}. Capital: {self.state.current_capital:.2f}")

        # --- End of Backtest ---
        logger.info("--- Backtest Run Finished ---")
        if active_trade:
             # Decide how to handle trades still open at the end (e.g., close at last price)
             logger.warning(f"Trade was still open at end of backtest: {active_trade}")
             # Optionally close it and record PnL based on last close price
             # ...

        # --- Generate Summary Report ---
        self.report_results()
        return self.state # Return final state including trade log


    def report_results(self):
        """Generates a basic summary report of the backtest."""
        logger.info("--- Backtest Results ---")
        num_trades = len(self.state.trade_log)
        if num_trades == 0:
            logger.info("No trades executed during backtest.")
            return

        wins = [t for t in self.state.trade_log if t.get('pnl', 0) > 0]
        losses = [t for t in self.state.trade_log if t.get('pnl', 0) < 0]
        win_rate = len(wins) / num_trades * 100 if num_trades > 0 else 0
        total_pnl = sum(t.get('pnl', 0) for t in self.state.trade_log)
        profit_factor = sum(t['pnl'] for t in wins) / abs(sum(t['pnl'] for t in losses)) if losses else float('inf')

        logger.info(f"Total Trades: {num_trades}")
        logger.info(f"Winning Trades: {len(wins)}")
        logger.info(f"Losing Trades: {len(losses)}")
        logger.info(f"Win Rate: {win_rate:.2f}%")
        logger.info(f"Total PnL: {total_pnl:.2f} USDT")
        logger.info(f"Final Capital: {self.state.current_capital:.2f} USDT")
        logger.info(f"Profit Factor: {profit_factor:.2f}")

        # TODO: Add more detailed analysis (e.g., Sharpe ratio, drawdown, plotting)

# ==============================================================================
# Main Execution Block
# ==============================================================================
if __name__ == '__main__':
    try:
        # --- VITAL PRE-RUN CHECKS ---
        if CONFIG["LIVE_TRADING"]:
            if CONFIG["API_KEY"] == 'YOUR_API_KEY' or CONFIG["API_SECRET"] == 'YOUR_API_SECRET':
                logger.error("!!! CRITICAL: API Key and Secret are required for LIVE TRADING but not set in CONFIG. Exiting. !!!")
                exit()
            logger.warning("<<<<< LIVE TRADING MODE ENABLED >>>>>")
        else:
             logger.info("<<<<< BACKTESTING MODE ENABLED >>>>>")


        logger.info("Configuration loaded:")
        for key, value in CONFIG.items():
            if "SECRET" not in key.upper() : logger.info(f"  {key}: {value}")


        # --- Instantiate the Chosen Strategy ---
        # <<< You can switch the strategy class here >>>
        strategy_to_use = DefaultMASRStrategy(CONFIG)
        # Example: strategy_to_use = MyOtherStrategy(CONFIG)


        # --- Select Mode: Live Trading or Backtesting ---
        if CONFIG["LIVE_TRADING"]:
            run_live_bot(CONFIG, strategy_to_use)
        else:
            # Initialize and run the backtester
            backtester = Backtester(CONFIG, strategy_to_use)
            backtester.run()

    except Exception as e:
        logger.critical(f"Failed to start bot or backtester: {e}", exc_info=True)