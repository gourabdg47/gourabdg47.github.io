import requests
import time
import numpy as np
from datetime import datetime, timedelta
from collections import deque
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# --- Configuration ---
SYMBOL = 'XRPUSDT'
DEPTH_LEVELS = 100          # Number of order book levels to fetch
REFRESH_INTERVAL = 5        # seconds - Increased interval slightly
HISTORY_MINUTES = 15        # Increased history for averages
CLUSTER_INTERVAL = 0.0005   # Price clustering interval for S/R from order book
ORDER_BOOK_HISTORY_SIZE = 10 # Number of recent order book snapshots to keep

# --- Strategy State Variables (Conceptual - Need external management) ---
# These would need to be managed outside the generate_signals function,
# potentially in the main loop or a dedicated state management class.
strategy_state = {
    "last_breakout_level": None,
    "last_breakout_direction": None, # "up" or "down"
    "impulse_start_price": None,
    "impulse_end_price": None,
    "in_pullback_phase": False,
    "confluence_zone_low": None,
    "confluence_zone_high": None,
    "confirmation_pattern": None, # e.g., "hammer", "shooting_star"
    "confirmation_candle_closed": False,
    "active_trade": None # Could store details of the current trade
}

# --- API Functions ---
def get_current_price():
    """Fetches the current mark price for the symbol."""
    url = 'https://fapi.binance.com/fapi/v1/ticker/price'
    try:
        response = requests.get(url, params={'symbol': SYMBOL}, timeout=5)
        response.raise_for_status() # Raise exception for bad status codes
        return float(response.json()['price'])
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error getting price: {e}")
    except Exception as e:
        print(f"{Fore.RED}Error processing price data: {e}")
    return None

def get_order_book():
    """Fetches the order book depth for the symbol."""
    url = 'https://fapi.binance.com/fapi/v1/depth'
    try:
        response = requests.get(url, params={'symbol': SYMBOL, 'limit': DEPTH_LEVELS}, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error getting order book: {e}")
    except Exception as e:
        print(f"{Fore.RED}Error processing order book data: {e}")
    return None

def get_fear_greed_index():
    """Gets Crypto Fear & Greed Index from Alternative.me."""
    try:
        url = 'https://api.alternative.me/fng/'
        # Using a common user-agent can sometimes help avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10) # Increased timeout
        response.raise_for_status()
        data = response.json()

        if 'data' in data and len(data['data']) > 0:
            return {
                'value': int(data['data'][0]['value']),
                'classification': data['data'][0]['value_classification']
            }
        print(f"{Fore.YELLOW}Warning: Unexpected F&G API response format.")
        return {'value': None, 'classification': 'N/A'}

    except requests.exceptions.Timeout:
        print(f"{Fore.YELLOW}Fear & Greed API Error: Request timed out.")
        return {'value': None, 'classification': 'Timeout'}
    except requests.exceptions.RequestException as e:
        print(f"{Fore.YELLOW}Fear & Greed API Error: {str(e)}")
        return {'value': None, 'classification': 'API Error'}
    except Exception as e:
        print(f"{Fore.YELLOW}Fear & Greed Processing Error: {str(e)}")
        return {'value': None, 'classification': 'Processing Error'}


# --- Metrics Calculation ---
def calculate_metrics(bids, asks, current_price):
    """Calculates various metrics from order book data."""
    if not bids or not asks:
        print(f"{Fore.YELLOW}Warning: Empty bids or asks received.")
        return None # Return None if data is invalid

    try:
        # Convert to float, handle potential errors if data isn't as expected
        bids_np = np.array(sorted([(float(p), float(q)) for p, q in bids], reverse=True))
        asks_np = np.array(sorted([(float(p), float(q)) for p, q in asks]))

        if bids_np.size == 0 or asks_np.size == 0:
             print(f"{Fore.YELLOW}Warning: Processed bids or asks array is empty.")
             return None

        total_bids_qty = bids_np[:,1].sum()
        total_asks_qty = asks_np[:,1].sum()
        total_liquidity = total_bids_qty + total_asks_qty

        if total_liquidity == 0:
            buy_pct = 50.0
            sell_pct = 50.0
            bs_ratio = 1.0
        else:
            buy_pct = (total_bids_qty / total_liquidity) * 100
            sell_pct = 100 - buy_pct
            bs_ratio = total_bids_qty / total_asks_qty if total_asks_qty != 0 else np.inf # Use infinity if no asks

        spread = asks_np[0][0] - bids_np[0][0]
        volatility = (spread / current_price) * 100 if current_price != 0 else 0

        bid_vwap = np.sum(bids_np[:,0] * bids_np[:,1]) / total_bids_qty if total_bids_qty != 0 else current_price
        ask_vwap = np.sum(asks_np[:,0] * asks_np[:,1]) / total_asks_qty if total_asks_qty != 0 else current_price
        mid_price = (bid_vwap + ask_vwap) / 2
        price_momentum = (bid_vwap - ask_vwap) / mid_price * 10000 if mid_price != 0 else 0 # Basis points momentum

        # --- Trend based on momentum ---
        if price_momentum > 50: trend = "Strong uptrend ▲▲"
        elif price_momentum > 15: trend = "Uptrend ▲"
        elif price_momentum < -50: trend = "Strong downtrend ▼▼"
        elif price_momentum < -15: trend = "Downtrend ▼"
        else: trend = "Neutral ➔"

        # --- Liquidity Clustering (Order Book S/R) ---
        def get_clusters(side_data):
            clusters = {}
            for price, qty in side_data:
                cluster_price = round(price / CLUSTER_INTERVAL) * CLUSTER_INTERVAL
                clusters[cluster_price] = clusters.get(cluster_price, 0) + qty
            # Sort by quantity (descending)
            return sorted(clusters.items(), key=lambda item: item[1], reverse=True)

        bid_clusters = get_clusters(bids_np)
        ask_clusters = get_clusters(asks_np)

        # Filter clusters to be relevant (support below price, resistance above)
        support_levels = [(p, v) for p, v in bid_clusters if p < current_price][:3]
        resistance_levels = [(p, v) for p, v in ask_clusters if p > current_price][:3]

        # --- Market Pressure ---
        if sell_pct > 55: market_pressure = "Strong selling"
        elif sell_pct > 51: market_pressure = "Moderate selling"
        elif buy_pct > 55: market_pressure = "Strong buying"
        elif buy_pct > 51: market_pressure = "Moderate buying"
        else: market_pressure = "Balanced"

        return {
            'current_price': current_price,
            'buy_pct': buy_pct,
            'sell_pct': sell_pct,
            'bs_ratio': bs_ratio,
            'volatility': volatility, # Based on spread
            'total_liquidity': total_liquidity,
            'liquidity_ratio': bs_ratio, # Same as bs_ratio here
            'support': support_levels, # From order book
            'resistance': resistance_levels, # From order book
            'trend': trend, # Based on order book momentum
            'price_momentum': price_momentum, # In basis points
            'market_pressure': market_pressure, # Based on buy/sell %
            'timestamp': datetime.now()
        }
    except Exception as e:
        print(f"{Fore.RED}Error calculating metrics: {e}")
        # You might want to log the bids/asks data here for debugging
        # print(f"Bids data: {bids}")
        # print(f"Asks data: {asks}")
        return None


# --- Signal Generation (FIB-SR-FVG Logic - Conceptual) ---
def generate_signals(current_price, historical_data, current_state):
    """
    Generates trading signals based on the FIB-SR-FVG Confluence Breakout Strategy.
    NOTE: This is a conceptual implementation. It requires historical OHLC data
          and external state management ('current_state') which are NOT provided
          by the base script's data fetching.

    Args:
        current_price (float): The current market price.
        historical_data (object): An object/dict containing necessary historical
                                   OHLC data, calculated Fib levels, identified
                                   FVGs, S/R levels, and breakout info.
                                   (NEEDS TO BE IMPLEMENTED SEPARATELY)
        current_state (dict): A dictionary holding the strategy's current state
                              (e.g., breakout detected, in pullback, etc.).
                              (NEEDS TO BE MANAGED EXTERNALLY)

    Returns:
        dict: A dictionary containing the signal information.
              Includes 'signal', 'direction', 'entry', 'target', 'stop_loss', 'reason'.
    """

    # --- Default Signal ---
    signal_info = {
        'signal': "Hold",
        'direction': "None",
        'entry': None,
        'target': None,
        'stop_loss': None,
        'reason': "No valid FIB-SR-FVG setup identified."
    }

    # --- Placeholder Checks (Replace with actual logic using historical_data and current_state) ---

    # --- 1. Breakout Detection (Requires Historical Data & State) ---
    # Example: Check if historical_data indicates a recent breakout occurred
    # and update current_state accordingly.
    # if historical_data.new_breakout_detected:
    #     current_state["last_breakout_level"] = historical_data.breakout_price
    #     current_state["last_breakout_direction"] = historical_data.breakout_direction # "up" or "down"
    #     current_state["impulse_start_price"] = historical_data.impulse_start
    #     current_state["impulse_end_price"] = historical_data.impulse_end
    #     current_state["in_pullback_phase"] = True
    #     current_state["confirmation_pattern"] = None
    #     current_state["confirmation_candle_closed"] = False
    #     print(f"DEBUG: Breakout {current_state['last_breakout_direction']} detected at {current_state['last_breakout_level']}")


    # --- 2. Pullback Phase ---
    if current_state.get("in_pullback_phase"):
        # print(f"DEBUG: In pullback phase. Current price: {current_price}")
        breakout_level = current_state.get("last_breakout_level")
        direction = current_state.get("last_breakout_direction")

        if not breakout_level or not direction:
             signal_info['reason'] = "State error: Missing breakout info during pullback."
             current_state["in_pullback_phase"] = False # Reset state
             return signal_info

        # --- 3. Confluence Zone Check (Requires Historical Data) ---
        # Example: Use historical_data to find Fib levels, historical S/R (near breakout_level), and FVGs.
        # Define confluence_zone_low, confluence_zone_high based on these elements.
        # is_in_confluence_zone = (confluence_zone_low <= current_price <= confluence_zone_high)
        # For demonstration, let's assume a hypothetical zone check:
        fib_level_example = breakout_level * (1 - 0.005) if direction == "up" else breakout_level * (1 + 0.005) # Example Fib 50% near breakout
        fvg_level_example = breakout_level * (1 - 0.004) if direction == "up" else breakout_level * (1 + 0.004) # Example FVG near breakout

        # Define a hypothetical confluence zone around the breakout level +/- tolerance
        tolerance = 0.003 * breakout_level # Example tolerance
        confluence_zone_low = min(breakout_level, fib_level_example, fvg_level_example) - tolerance
        confluence_zone_high = max(breakout_level, fib_level_example, fvg_level_example) + tolerance
        current_state["confluence_zone_low"] = confluence_zone_low # Store for potential SL calculation
        current_state["confluence_zone_high"] = confluence_zone_high # Store for potential SL calculation


        is_in_confluence_zone = (confluence_zone_low <= current_price <= confluence_zone_high)
        # print(f"DEBUG: Confluence Zone [{confluence_zone_low:.5f} - {confluence_zone_high:.5f}]. In Zone: {is_in_confluence_zone}")


        if is_in_confluence_zone:
            # --- 4. Confirmation Pattern Check (Requires Historical Candlestick Data) ---
            # Example: Check historical_data for a bullish/bearish reversal pattern
            # (Hammer, Engulfing, etc.) within the last N candles ending at the confluence zone.
            # if historical_data.has_confirmation_pattern:
            #    current_state["confirmation_pattern"] = historical_data.pattern_name
            #    current_state["confirmation_pattern_low"] = historical_data.pattern_low # For SL
            #    current_state["confirmation_pattern_high"] = historical_data.pattern_high # For SL
            #    print(f"DEBUG: Confirmation pattern '{current_state['confirmation_pattern']}' detected.")

            # --- 5. Confirmation Candle Check (Requires Historical Candlestick Data) ---
            # Example: Check if the *next* candle after the pattern closed confirming the direction.
            # if current_state["confirmation_pattern"] and historical_data.is_pattern_confirmed:
            #    current_state["confirmation_candle_closed"] = True
            #    print(f"DEBUG: Confirmation candle closed.")


            # --- 6. Generate Signal ---
            # For this conceptual example, let's assume confirmation is met if price simply *touches* the zone
            # AND the original order book momentum aligns (a weak substitute for real confirmation).
            # THIS IS A MAJOR SIMPLIFICATION - REAL IMPLEMENTATION NEEDS CANDLE PATTERNS.

            # Placeholder: Use order book trend as a very weak proxy for confirmation direction
            order_book_metrics = calculate_metrics(get_order_book().get('bids', []), get_order_book().get('asks', []), current_price) # Recalculate for current trend
            order_book_trend = order_book_metrics['trend'] if order_book_metrics else "Neutral"

            # --- Generate LONG Signal ---
            if direction == "up" and 'up' in order_book_trend.lower(): # Conceptual confirmation
                 # Assume confirmation pattern low is near confluence_zone_low for SL calc
                 pattern_low_example = confluence_zone_low * 0.9995
                 # Assume next resistance is 1% higher for TP calc
                 target_resistance_example = current_price * 1.01

                 signal_info = {
                    'signal': "Buy",
                    'direction': "Long",
                    'entry': current_price, # Enter at market after 'confirmation'
                    'target': target_resistance_example, # Placeholder TP
                    'stop_loss': pattern_low_example, # Placeholder SL below pattern/zone
                    'reason': f"Breakout above {breakout_level:.5f}, pullback to confluence [{confluence_zone_low:.5f}-{confluence_zone_high:.5f}], weak confirmation (OB Up)."
                 }
                 print(f"{Fore.GREEN}>>> LONG Signal Generated: {signal_info['reason']}")
                 current_state["in_pullback_phase"] = False # Reset state after signal
                 current_state["active_trade"] = signal_info # Track trade

            # --- Generate SHORT Signal ---
            elif direction == "down" and 'down' in order_book_trend.lower(): # Conceptual confirmation
                 # Assume confirmation pattern high is near confluence_zone_high for SL calc
                 pattern_high_example = confluence_zone_high * 1.0005
                 # Assume next support is 1% lower for TP calc
                 target_support_example = current_price * 0.99

                 signal_info = {
                    'signal': "Sell",
                    'direction': "Short",
                    'entry': current_price, # Enter at market after 'confirmation'
                    'target': target_support_example, # Placeholder TP
                    'stop_loss': pattern_high_example, # Placeholder SL above pattern/zone
                    'reason': f"Breakdown below {breakout_level:.5f}, pullback to confluence [{confluence_zone_low:.5f}-{confluence_zone_high:.5f}], weak confirmation (OB Down)."
                 }
                 print(f"{Fore.RED}>>> SHORT Signal Generated: {signal_info['reason']}")
                 current_state["in_pullback_phase"] = False # Reset state after signal
                 current_state["active_trade"] = signal_info # Track trade
            else:
                 signal_info['reason'] = f"In confluence zone [{confluence_zone_low:.5f}-{confluence_zone_high:.5f}] but waiting for confirmation."


        # Add logic here to reset pullback phase if price moves too far away
        # from the breakout level without confirming.
        # Example:
        # elif (direction == "up" and current_price < confluence_zone_low * 0.995) or \
        #      (direction == "down" and current_price > confluence_zone_high * 1.005):
        #     print(f"DEBUG: Pullback failed/moved too far. Resetting state.")
        #     current_state["in_pullback_phase"] = False


    # --- Add logic to manage active trade (e.g., check SL/TP) ---
    # if current_state.get("active_trade"):
    #     trade = current_state["active_trade"]
    #     if trade['direction'] == "Long" and current_price >= trade['target']:
    #         print(f"{Fore.GREEN}>>> TP Hit for LONG trade")
    #         current_state["active_trade"] = None
    #     elif trade['direction'] == "Long" and current_price <= trade['stop_loss']:
    #         print(f"{Fore.RED}>>> SL Hit for LONG trade")
    #         current_state["active_trade"] = None
    #     # Add similar checks for SHORT trades

    return signal_info


# --- Main Loop ---
def main():
    history = [] # For calculating average buy/sell % over time
    recent_order_books = deque(maxlen=ORDER_BOOK_HISTORY_SIZE)
    signal_history = deque(maxlen=10) # Keep history of generated signals

    global strategy_state # Allow modification of the global state dictionary

    while True:
        start_time = time.time()

        # --- Fetch Data ---
        current_price = get_current_price()
        order_book = get_order_book()
        fgi = get_fear_greed_index() # Fetch F&G index

        if not current_price or not order_book or 'bids' not in order_book or 'asks' not in order_book:
            print(f"{Fore.YELLOW}Waiting for valid market data...")
            time.sleep(REFRESH_INTERVAL)
            continue

        # --- Calculate Order Book Metrics ---
        metrics = calculate_metrics(order_book['bids'], order_book['asks'], current_price)
        if not metrics: # Skip iteration if metrics calculation failed
             time.sleep(REFRESH_INTERVAL)
             continue

        recent_order_books.appendleft(metrics) # Store current metrics snapshot

        # --- Generate Signals (Using Conceptual Function) ---
        # !!! IMPORTANT: This requires providing 'historical_data' and managing 'strategy_state' !!!
        # You would need to implement fetching/processing historical data here.
        # For now, we pass None for historical_data and use the global strategy_state.
        signals = generate_signals(current_price, None, strategy_state) # Pass state
        signal_history.append(signals) # Store the generated signal info

        # --- Update History for Averages ---
        history.append((metrics['timestamp'], metrics['buy_pct'], metrics['sell_pct']))
        cutoff_time = datetime.now() - timedelta(minutes=HISTORY_MINUTES)
        history = [h for h in history if h[0] > cutoff_time] # Keep only recent history

        # --- Calculate Averages ---
        buy_history_pct = [h[1] for h in history]
        sell_history_pct = [h[2] for h in history]
        avg_buy = np.mean(buy_history_pct) if buy_history_pct else 50.0
        avg_sell = np.mean(sell_history_pct) if sell_history_pct else 50.0

        # --- Display Information ---
        print("\033c", end="") # Clear screen

        # Header
        print(f"\n{Fore.CYAN}=== REAL-TIME {SYMBOL} FUTURES ANALYSIS (FIB-SR-FVG Logic) ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Last Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")

        # Trading Signals Section (New Format)
        print(f"\n{Fore.MAGENTA}TRADING SIGNAL ({'Conceptual - Needs Historical Data'}):{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'Signal':<8} | {'Direction':<10} | {'Entry':<12} | {'Target':<12} | {'Stop Loss':<12}")
        print("-" * 65)

        sig = signals['signal']
        direction = signals['direction']
        entry_p = f"{signals['entry']:.5f}" if signals['entry'] else "N/A"
        target_p = f"{signals['target']:.5f}" if signals['target'] else "N/A"
        stop_p = f"{signals['stop_loss']:.5f}" if signals['stop_loss'] else "N/A"

        sig_color = Fore.GREEN if sig == "Buy" else Fore.RED if sig == "Sell" else Fore.YELLOW
        dir_color = Fore.GREEN if direction == "Long" else Fore.RED if direction == "Short" else Fore.YELLOW

        print(f"{sig_color}{sig:<8}{Style.RESET_ALL} | "
              f"{dir_color}{direction:<10}{Style.RESET_ALL} | "
              f"{Fore.WHITE}{entry_p:<12} | "
              f"{Fore.GREEN}{target_p:<12} | "
              f"{Fore.RED}{stop_p:<12}")
        print(f"{Fore.CYAN}Reason: {signals['reason']}") # Display the reason

        # Order Book History (Unchanged)
        print(f"\n{Fore.MAGENTA}LAST {len(recent_order_books)} ORDER BOOK UPDATES ({HISTORY_MINUTES} min avg):{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'Time':<10} | {'Buy %':<8} | {'Sell %':<8} | {'Pressure':<16} | {'Trend (OB Mom.)'}")
        print("-" * 75)
        for entry in recent_order_books:
            time_str = entry['timestamp'].strftime("%H:%M:%S")
            buy_color = Fore.GREEN if entry['buy_pct'] > 51 else Fore.YELLOW if entry['buy_pct'] > 49 else Fore.RED
            sell_color = Fore.RED if entry['sell_pct'] > 51 else Fore.YELLOW if entry['sell_pct'] > 49 else Fore.GREEN
            trend_color = Fore.GREEN if 'up' in entry['trend'].lower() else Fore.RED if 'down' in entry['trend'].lower() else Fore.YELLOW
            pressure_color = Fore.GREEN if 'buy' in entry['market_pressure'].lower() else Fore.RED if 'sell' in entry['market_pressure'].lower() else Fore.YELLOW

            print(f"{Fore.WHITE}{time_str:<10} | "
                  f"{buy_color}{entry['buy_pct']:6.2f}%{Style.RESET_ALL} | "
                  f"{sell_color}{entry['sell_pct']:6.2f}%{Style.RESET_ALL} | "
                  f"{pressure_color}{entry['market_pressure']:<16}{Style.RESET_ALL} | "
                  f"{trend_color}{entry['trend']}")
        print(f"{Fore.CYAN}Avg last {HISTORY_MINUTES} min: Buy: {avg_buy:.2f}% | Sell: {avg_sell:.2f}%")


        # Current Market Snapshot (Unchanged)
        print(f"\n{Fore.MAGENTA}CURRENT MARKET SNAPSHOT:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Price: {Fore.YELLOW}${metrics['current_price']:.5f}   "
              f"Buy/Sell Ratio (Qty): {Fore.CYAN}{metrics['bs_ratio']:.2f}")
        print(f"OB Pressure: {Fore.GREEN if 'buy' in metrics['market_pressure'] else Fore.RED}{metrics['market_pressure']} "
              f"({Fore.GREEN}{metrics['buy_pct']:.1f}%{Style.RESET_ALL} / {Fore.RED}{metrics['sell_pct']:.1f}%{Style.RESET_ALL})")
        print(f"OB Momentum Trend: {trend_color}{metrics['trend']} "
              f"({Fore.CYAN}{metrics['price_momentum']:+.1f} bps{Style.RESET_ALL})")
        print(f"Spread Volatility: {Fore.WHITE}{metrics['volatility']:.4f}%")


        # Liquidity Analysis (Order Book Based S/R)
        print(f"\n{Fore.MAGENTA}ORDER BOOK LIQUIDITY ANALYSIS:{Style.RESET_ALL}")
        print(f"Total Liq: {Fore.WHITE}{metrics['total_liquidity']:,.0f} {SYMBOL}")
        print(f"{Fore.GREEN}Support Levels (Order Book Clusters):{Style.RESET_ALL}")
        for p, v in metrics['support']: print(f"  ${p:<10.5f} - {Fore.WHITE}{v:,.0f}")
        print(f"{Fore.RED}Resistance Levels (Order Book Clusters):{Style.RESET_ALL}")
        for p, v in metrics['resistance']: print(f"  ${p:<10.5f} - {Fore.WHITE}{v:,.0f}")

        # Fear & Greed Index
        print(f"\n{Fore.MAGENTA}MARKET SENTIMENT (Alternative.me):{Style.RESET_ALL}")
        if fgi['value'] is not None:
            if fgi['value'] >= 75: color, sentiment = Fore.LIGHTGREEN_EX, "Extreme Greed"
            elif fgi['value'] >= 55: color, sentiment = Fore.GREEN, "Greed"
            elif fgi['value'] <= 25: color, sentiment = Fore.LIGHTRED_EX, "Extreme Fear"
            elif fgi['value'] <= 45: color, sentiment = Fore.RED, "Fear"
            else: color, sentiment = Fore.YELLOW, "Neutral"
            print(f"{color}Fear & Greed Index: {fgi['value']} ({sentiment} - {fgi['classification']})")
        else:
            print(f"{Fore.YELLOW}Fear & Greed Index: Data unavailable ({fgi['classification']})")


        # --- Loop Timing ---
        elapsed_time = time.time() - start_time
        sleep_time = max(0, REFRESH_INTERVAL - elapsed_time)
        time.sleep(sleep_time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Analysis terminated by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}An unexpected error occurred in main loop: {e}")
        # Consider adding more detailed logging here, e.g., traceback
        import traceback
        traceback.print_exc()

