import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests
import time
from abc import ABC, abstractmethod

class Strategy(ABC):
    """Abstract base class for trading strategies"""
    
    def __init__(self, params=None):
        self.params = params or {}
        
    @abstractmethod
    def calculate_indicators(self, df):
        """Calculate indicators needed for the strategy"""
        pass
        
    @abstractmethod
    def generate_signals(self, df):
        """Generate buy/sell signals based on indicators"""
        pass
    
    def get_param_summary(self):
        """Return a summary of strategy parameters"""
        return "\n".join([f"{k}: {v}" for k, v in self.params.items()])


class MAXRSIStrategy(Strategy):
    """Moving Average Crossover + RSI + Support/Resistance strategy"""
    
    def __init__(self, params=None):
        default_params = {
            'FAST_MA': 9,
            'SLOW_MA': 21,
            'SR_PERIOD': 24,
            'RSI_PERIOD': 14,
            'RSI_MID': 50
        }
        # Override defaults with any provided parameters
        if params:
            default_params.update(params)
        super().__init__(default_params)
    
    def calculate_rsi(self, series, period):
        delta = series.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
        
    def calculate_indicators(self, df):
        # Calculate moving averages
        df['fast_ma'] = df['close'].rolling(window=self.params['FAST_MA']).mean()
        df['slow_ma'] = df['close'].rolling(window=self.params['SLOW_MA']).mean()
        
        # Calculate support and resistance based on SR_PERIOD
        df['support'] = df['close'].rolling(window=self.params['SR_PERIOD']).min()
        df['resistance'] = df['close'].rolling(window=self.params['SR_PERIOD']).max()
        
        # Calculate RSI
        df['rsi'] = self.calculate_rsi(df['close'], period=self.params['RSI_PERIOD'])
        
        # Calculate signal strength components
        df['signal_strength'] = 0
        
        # 1. Trend based on MA Crossover
        df.loc[df['fast_ma'] > df['slow_ma'], 'signal_strength'] += 1
        df.loc[df['fast_ma'] < df['slow_ma'], 'signal_strength'] -= 1
        
        # 2. Support/Resistance Break
        df.loc[df['close'] > df['resistance'], 'signal_strength'] += 1
        df.loc[df['close'] < df['support'], 'signal_strength'] -= 1
        
        # 3. RSI Confirmation
        df.loc[df['rsi'] > self.params['RSI_MID'], 'signal_strength'] += 1
        df.loc[df['rsi'] < self.params['RSI_MID'], 'signal_strength'] -= 1
        
        # Generate trend signals for analysis
        df['ma_trend'] = None
        df.loc[df['fast_ma'] > df['slow_ma'], 'ma_trend'] = 'bullish'
        df.loc[df['fast_ma'] < df['slow_ma'], 'ma_trend'] = 'bearish'
        
        df['rsi_trend'] = None
        df.loc[df['rsi'] > self.params['RSI_MID'], 'rsi_trend'] = 'bullish'
        df.loc[df['rsi'] < self.params['RSI_MID'], 'rsi_trend'] = 'bearish'
        
        return df
    
    def generate_signals(self, df):
        """Generate final trading signals based on the conditions"""
        df['signal'] = None
        
        # Buy condition: signal_strength >= 2 AND MA trend is bullish AND RSI trend is bullish
        buy_mask = (df['signal_strength'] >= 2) & (df['ma_trend'] == 'bullish') & (df['rsi_trend'] == 'bullish')
        df.loc[buy_mask, 'signal'] = 'buy'
        
        # Sell condition: signal_strength <= -2 AND MA trend is bearish AND RSI trend is bearish
        sell_mask = (df['signal_strength'] <= -2) & (df['ma_trend'] == 'bearish') & (df['rsi_trend'] == 'bearish')
        df.loc[sell_mask, 'signal'] = 'sell'
        
        return df
    
    def plot_indicators(self, df, ax):
        """Plot strategy-specific indicators"""
        ax.plot(df['timestamp'], df['fast_ma'], label=f"{self.params['FAST_MA']} MA", alpha=0.7)
        ax.plot(df['timestamp'], df['slow_ma'], label=f"{self.params['SLOW_MA']} MA", alpha=0.7)
        ax.plot(df['timestamp'], df['support'], '--', label='Support', alpha=0.5)
        ax.plot(df['timestamp'], df['resistance'], '--', label='Resistance', alpha=0.5)
        
        # Return the secondary indicator to plot
        return {
            'title': 'RSI Indicator',
            'data': df['rsi'],
            'color': 'purple',
            'label': 'RSI',
            'references': [
                {'value': self.params['RSI_MID'], 'color': 'black', 'alpha': 0.5},
                {'value': 70, 'color': 'red', 'alpha': 0.5},
                {'value': 30, 'color': 'green', 'alpha': 0.5}
            ]
        }


class SimpleEMAStrategy(Strategy):
    """Simple EMA Crossover Strategy"""
    
    def __init__(self, params=None):
        default_params = {
            'FAST_EMA': 12,
            'SLOW_EMA': 26,
            'SIGNAL_EMA': 9  # For MACD
        }
        # Override defaults with any provided parameters
        if params:
            default_params.update(params)
        super().__init__(default_params)
    
    def calculate_indicators(self, df):
        # Calculate EMAs
        df['fast_ema'] = df['close'].ewm(span=self.params['FAST_EMA'], adjust=False).mean()
        df['slow_ema'] = df['close'].ewm(span=self.params['SLOW_EMA'], adjust=False).mean()
        
        # Calculate MACD
        df['macd'] = df['fast_ema'] - df['slow_ema']
        df['signal_line'] = df['macd'].ewm(span=self.params['SIGNAL_EMA'], adjust=False).mean()
        df['macd_histogram'] = df['macd'] - df['signal_line']
        
        return df
    
    def generate_signals(self, df):
        df['signal'] = None
        
        # Generate signals - buy when MACD crosses above signal line
        signal_cross_up = (df['macd'] > df['signal_line']) & (df['macd'].shift(1) <= df['signal_line'].shift(1))
        signal_cross_down = (df['macd'] < df['signal_line']) & (df['macd'].shift(1) >= df['signal_line'].shift(1))
        
        df.loc[signal_cross_up, 'signal'] = 'buy'
        df.loc[signal_cross_down, 'signal'] = 'sell'
        
        return df
    
    def plot_indicators(self, df, ax):
        """Plot strategy-specific indicators"""
        ax.plot(df['timestamp'], df['fast_ema'], label=f"{self.params['FAST_EMA']} EMA", alpha=0.7)
        ax.plot(df['timestamp'], df['slow_ema'], label=f"{self.params['SLOW_EMA']} EMA", alpha=0.7)
        
        # Return the secondary indicator to plot
        return {
            'title': 'MACD',
            'data': df['macd'],
            'color': 'blue',
            'label': 'MACD',
            'overlay': [
                {'data': df['signal_line'], 'color': 'red', 'label': 'Signal'},
                {'data': df['macd_histogram'], 'type': 'bar', 'color': 'green', 'label': 'Histogram'}
            ]
        }


class BacktestResults:
    def __init__(self, initial_capital, risk_params):
        self.trades = []
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.active_position = None
        self.risk_params = risk_params  # Dictionary with risk params
        
    def add_trade(self, trade):
        self.trades.append(trade)
        
    def calculate_statistics(self):
        """Calculate comprehensive trading statistics from backtest results"""
        if not self.trades:
            return {
                'total_trades': 0,
                'win_rate': 0,
                'profit_factor': 0,
                'total_profit_pct': 0,
                'max_drawdown_pct': 0,
                'avg_trade_pct': 0,
                'sharpe_ratio': 0
            }
            
        # Create DataFrame for analysis
        trade_df = pd.DataFrame(self.trades)
        
        # Basic trade analysis
        wins = trade_df[trade_df['pnl'] > 0]
        losses = trade_df[trade_df['pnl'] <= 0]
        
        total_profit = trade_df['pnl'].sum()
        gross_profit = wins['pnl'].sum() if not wins.empty else 0
        gross_loss = abs(losses['pnl'].sum()) if not losses.empty else 1  # Avoid division by zero
        
        # Calculate running balance and drawdown
        balances = [self.initial_capital]
        for trade in self.trades:
            balances.append(balances[-1] + trade['pnl'])
        
        # Calculate max drawdown
        balance_series = pd.Series(balances)
        running_max = balance_series.cummax()
        drawdown = (running_max - balance_series) / running_max
        max_drawdown = drawdown.max()
        
        # Calculate daily returns for Sharpe ratio
        if len(self.trades) > 1:
            trade_df['date'] = pd.to_datetime(trade_df['exit_time']).dt.date
            daily_pnl = trade_df.groupby('date')['pnl'].sum()
            daily_returns = daily_pnl / self.initial_capital
            sharpe = np.mean(daily_returns) / np.std(daily_returns) * np.sqrt(252) if np.std(daily_returns) > 0 else 0
            sortino = np.mean(daily_returns) / np.std(daily_returns[daily_returns < 0]) * np.sqrt(252) if np.std(daily_returns[daily_returns < 0]) > 0 else 0
        else:
            sharpe = 0
            sortino = 0
        
        # Calculate more detailed metrics
        avg_win = wins['pnl'].mean() if not wins.empty else 0
        avg_loss = losses['pnl'].mean() if not losses.empty else 0
        max_win = wins['pnl'].max() if not wins.empty else 0
        max_loss = losses['pnl'].min() if not losses.empty else 0
        
        # Calculate average holding time
        if not trade_df.empty:
            trade_df['holding_time'] = (trade_df['exit_time'] - trade_df['entry_time']).dt.total_seconds() / 60
            avg_holding_time = trade_df['holding_time'].mean()
            max_holding_time = trade_df['holding_time'].max()
            min_holding_time = trade_df['holding_time'].min()
        else:
            avg_holding_time = 0
            max_holding_time = 0
            min_holding_time = 0
        
        # Calculate consecutive wins/losses
        if not trade_df.empty:
            trade_df['win'] = trade_df['pnl'] > 0
            trade_df['streak'] = (trade_df['win'] != trade_df['win'].shift()).cumsum()
            win_streaks = trade_df[trade_df['win']].groupby('streak').size()
            loss_streaks = trade_df[~trade_df['win']].groupby('streak').size()
            
            max_win_streak = win_streaks.max() if not win_streaks.empty else 0
            max_loss_streak = loss_streaks.max() if not loss_streaks.empty else 0
        else:
            max_win_streak = 0
            max_loss_streak = 0
        
        # Monthly performance
        if not trade_df.empty:
            trade_df['year_month'] = pd.to_datetime(trade_df['exit_time']).dt.strftime('%Y-%m')
            monthly_returns = trade_df.groupby('year_month')['pnl'].sum() / self.initial_capital * 100
            best_month = monthly_returns.max() if not monthly_returns.empty else 0
            worst_month = monthly_returns.min() if not monthly_returns.empty else 0
            
            # Monthly statistics
            monthly_stats = {
                'mean': monthly_returns.mean() if not monthly_returns.empty else 0,
                'median': monthly_returns.median() if not monthly_returns.empty else 0,
                'std': monthly_returns.std() if not monthly_returns.empty else 0,
                'best': best_month,
                'worst': worst_month
            }
        else:
            monthly_stats = {
                'mean': 0, 'median': 0, 'std': 0, 'best': 0, 'worst': 0
            }
        
        # Expectancy and risk/reward metrics
        expectancy = ((avg_win * len(wins)) + (avg_loss * len(losses))) / len(self.trades) if self.trades else 0
        if avg_loss != 0:
            reward_risk_ratio = abs(avg_win / avg_loss) if avg_loss else 0
        else:
            reward_risk_ratio = float('inf') if avg_win > 0 else 0
        
        # Return on risk calculations
        if 'RISK_PER_TRADE' in self.risk_params:
            total_risk = self.initial_capital * self.risk_params['RISK_PER_TRADE'] * len(self.trades)
            return_on_risk = total_profit / total_risk if total_risk > 0 else 0
        else:
            return_on_risk = 0
                
        # Combine all statistics
        return {
            # Basic statistics
            'total_trades': len(self.trades),
            'winning_trades': len(wins),
            'losing_trades': len(losses),
            'breakeven_trades': len(trade_df[trade_df['pnl'] == 0]),
            'win_rate': len(wins) / len(self.trades) if self.trades else 0,
            'profit_factor': gross_profit / gross_loss if gross_loss else gross_profit,
            
            # Profit metrics
            'total_profit': total_profit,
            'total_profit_pct': (total_profit / self.initial_capital) * 100,
            'gross_profit': gross_profit,
            'gross_loss': -gross_loss,
            
            # Risk metrics
            'max_drawdown_pct': max_drawdown * 100,
            'avg_trade_pct': (total_profit / self.initial_capital / len(self.trades)) * 100 if self.trades else 0,
            'return_on_risk': return_on_risk,
            'risk_reward_ratio': reward_risk_ratio,
            
            # Trade metrics
            'avg_win': avg_win,
            'avg_loss': avg_loss,
            'max_win': max_win,
            'max_loss': max_loss,
            'expectancy': expectancy,
            
            # Time metrics
            'avg_holding_time_min': avg_holding_time,
            'max_holding_time_min': max_holding_time,
            'min_holding_time_min': min_holding_time,
            
            # Streak metrics
            'max_win_streak': max_win_streak,
            'max_loss_streak': max_loss_streak,
            
            # Performance ratios
            'sharpe_ratio': sharpe,
            'sortino_ratio': sortino,
            
            # Monthly performance
            'monthly_stats': monthly_stats,
            
            # Final balance
            'final_capital': self.initial_capital + total_profit,
            'final_return_pct': (total_profit / self.initial_capital) * 100,
            
            # Exit reason breakdown
            'exit_reasons': trade_df['exit_reason'].value_counts().to_dict() if not trade_df.empty else {}
        }


class DataProvider:
    """Class for fetching and managing market data"""
    
    @staticmethod
    def get_historical_data(symbol, timeframe, days_back=30):
        """Fetch historical data from Binance API"""
        # Get current date and specified days earlier
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        # Format timestamps for API request
        start_ts = int(start_date.timestamp() * 1000)
        end_ts = int(end_date.timestamp() * 1000)
        
        # Fetch data from Binance API
        url = f"https://api.binance.com/api/v3/klines"
        params = {
            'symbol': symbol,
            'interval': timeframe,
            'startTime': start_ts,
            'endTime': end_ts,
            'limit': 1000  # Maximum allowed
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Convert to DataFrame
            df = pd.DataFrame(data, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_asset_volume', 'trades', 
                'taker_buy_base', 'taker_buy_quote', 'ignore'
            ])
            
            # Convert types
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            for col in ['open', 'high', 'low', 'close', 'volume']:
                df[col] = df[col].astype(float)
                
            print(f"Fetched {len(df)} candles from {df['timestamp'].min()} to {df['timestamp'].max()}")
            return df
            
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return pd.DataFrame()


class Backtester:
    """Main backtesting engine"""
    
    def __init__(self, 
                 symbol, 
                 timeframe, 
                 strategy, 
                 initial_capital=20.0, 
                 leverage=5.0,
                 risk_per_trade=0.01,
                 target_pct=0.02,
                 stop_loss_pct=0.01):
        
        self.symbol = symbol
        self.timeframe = timeframe
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.leverage = leverage
        self.risk_per_trade = risk_per_trade
        self.target_pct = target_pct
        self.stop_loss_pct = stop_loss_pct
        
        # Create risk parameters dictionary
        self.risk_params = {
            'LEVERAGE': leverage,
            'RISK_PER_TRADE': risk_per_trade,
            'TARGET_PCT': target_pct,
            'STOP_LOSS_PCT': stop_loss_pct
        }
        
        # Initialize results
        self.results = None
        self.df = None
    
    def run(self, data=None, days_back=30):
        """Run backtest with provided data or fetch new data"""
        # Get data if not provided
        if data is None:
            self.df = DataProvider.get_historical_data(self.symbol, self.timeframe, days_back)
        else:
            self.df = data.copy()
            
        if self.df.empty:
            print("No data available for backtesting.")
            return None
            
        # Calculate indicators and generate signals
        self.df = self.strategy.calculate_indicators(self.df)
        self.df = self.strategy.generate_signals(self.df)
        
        # Initialize results object
        self.results = BacktestResults(self.initial_capital, self.risk_params)
        
        # Execute the backtest
        self._execute_backtest()
        
        return self.results
    
    def _execute_backtest(self):
        """Core backtesting logic to process signals and manage positions"""
        for i in range(len(self.df)):
            current_row = self.df.iloc[i]
            current_price = current_row['close']
            current_time = current_row['timestamp']
            signal = current_row['signal']
            
            # Check if we have an active position
            if self.results.active_position:
                # Check if stop loss or take profit hit
                position = self.results.active_position
                
                if position['side'] == 'buy':
                    # Check take profit
                    if current_price >= position['take_profit']:
                        pnl = (position['size'] * (current_price - position['entry']))
                        self.results.add_trade({
                            'entry_time': position['time'],
                            'exit_time': current_time,
                            'side': position['side'],
                            'entry': position['entry'],
                            'exit': current_price,
                            'size': position['size'],
                            'pnl': pnl,
                            'exit_reason': 'take_profit'
                        })
                        self.results.current_capital += pnl
                        self.results.active_position = None
                        
                    # Check stop loss
                    elif current_price <= position['stop_loss']:
                        pnl = (position['size'] * (current_price - position['entry']))
                        self.results.add_trade({
                            'entry_time': position['time'],
                            'exit_time': current_time,
                            'side': position['side'],
                            'entry': position['entry'],
                            'exit': current_price,
                            'size': position['size'],
                            'pnl': pnl,
                            'exit_reason': 'stop_loss'
                        })
                        self.results.current_capital += pnl
                        self.results.active_position = None
                        
                elif position['side'] == 'sell':
                    # Check take profit
                    if current_price <= position['take_profit']:
                        pnl = (position['size'] * (position['entry'] - current_price))
                        self.results.add_trade({
                            'entry_time': position['time'],
                            'exit_time': current_time,
                            'side': position['side'],
                            'entry': position['entry'],
                            'exit': current_price,
                            'size': position['size'],
                            'pnl': pnl,
                            'exit_reason': 'take_profit'
                        })
                        self.results.current_capital += pnl
                        self.results.active_position = None
                        
                    # Check stop loss
                    elif current_price >= position['stop_loss']:
                        pnl = (position['size'] * (position['entry'] - current_price))
                        self.results.add_trade({
                            'entry_time': position['time'],
                            'exit_time': current_time,
                            'side': position['side'],
                            'entry': position['entry'],
                            'exit': current_price,
                            'size': position['size'],
                            'pnl': pnl,
                            'exit_reason': 'stop_loss'
                        })
                        self.results.current_capital += pnl
                        self.results.active_position = None
            
            # If no active position and we have a signal, open a new position
            elif signal and not self.results.active_position:
                # Calculate position size
                capital_to_risk = self.results.current_capital * self.risk_per_trade
                position_size_coins = capital_to_risk / (current_price * (self.stop_loss_pct / self.leverage))
                
                if position_size_coins <= 0:
                    continue  # Skip if position size calculation is invalid
                    
                if signal == 'buy':
                    stop_loss = current_price * (1 - self.stop_loss_pct/self.leverage)
                    take_profit = current_price * (1 + self.target_pct/self.leverage)
                    
                    self.results.active_position = {
                        'time': current_time,
                        'side': 'buy',
                        'entry': current_price,
                        'stop_loss': stop_loss,
                        'take_profit': take_profit,
                        'size': position_size_coins
                    }
                    
                elif signal == 'sell':
                    stop_loss = current_price * (1 + self.stop_loss_pct/self.leverage)
                    take_profit = current_price * (1 - self.target_pct/self.leverage)
                    
                    self.results.active_position = {
                        'time': current_time,
                        'side': 'sell',
                        'entry': current_price,
                        'stop_loss': stop_loss,
                        'take_profit': take_profit,
                        'size': position_size_coins
                    }
        
        # Close any remaining positions at the last price
        if self.results.active_position:
            position = self.results.active_position
            last_price = self.df.iloc[-1]['close']
            
            if position['side'] == 'buy':
                pnl = (position['size'] * (last_price - position['entry']))
            else:
                pnl = (position['size'] * (position['entry'] - last_price))
                
            self.results.add_trade({
                'entry_time': position['time'],
                'exit_time': self.df.iloc[-1]['timestamp'],
                'side': position['side'],
                'entry': position['entry'],
                'exit': last_price,
                'size': position['size'],
                'pnl': pnl,
                'exit_reason': 'backtest_end'
            })
            self.results.current_capital += pnl
    
    def display_results(self):
        """Display detailed backtest results in a formatted way"""
        if not self.results:
            print("No backtest results to display. Run the backtest first.")
            return
            
        stats = self.results.calculate_statistics()
        
        print("\n" + "="*80)
        print(f"BACKTESTING RESULTS FOR {self.symbol} ({self.timeframe} timeframe)")
        print("="*80)
        
        print(f"\nSTRATEGY PARAMETERS:")
        print(f"Strategy Type: {self.strategy.__class__.__name__}")
        print(self.strategy.get_param_summary())
        print(f"\nRISK PARAMETERS:")
        print(f"Risk Per Trade: {self.risk_per_trade*100}%, Stop Loss: {self.stop_loss_pct*100}%")
        print(f"Target Profit: {self.target_pct*100}%, Leverage: {self.leverage}x")
        print(f"Initial Capital: ${self.initial_capital:.2f}")
        
        print("\nPERFORMANCE SUMMARY:")
        print(f"Final Capital: ${stats['final_capital']:.2f} (Initial: ${self.initial_capital:.2f})")
        print(f"Total Return: ${stats['total_profit']:.2f} ({stats['total_profit_pct']:.2f}%)")
        print(f"Maximum Drawdown: {stats['max_drawdown_pct']:.2f}%")
        
        print("\nRISK-ADJUSTED PERFORMANCE:")
        print(f"Sharpe Ratio: {stats['sharpe_ratio']:.2f}")
        print(f"Sortino Ratio: {stats['sortino_ratio']:.2f}")
        print(f"Profit Factor: {stats['profit_factor']:.2f}")
        print(f"Return on Risk: {stats['return_on_risk']:.2f}")
        print(f"Reward/Risk Ratio: {stats['risk_reward_ratio']:.2f}")
        
        print("\nTRADE STATISTICS:")
        print(f"Total Trades: {stats['total_trades']}")
        print(f"Win Rate: {stats['win_rate']*100:.2f}% ({stats['winning_trades']} wins, {stats['losing_trades']} losses)")
        print(f"Average Trade Return: {stats['avg_trade_pct']:.2f}%")
        print(f"Average Win: ${stats['avg_win']:.2f}")
        print(f"Average Loss: ${stats['avg_loss']:.2f}")
        print(f"Largest Win: ${stats['max_win']:.2f}")
        print(f"Largest Loss: ${stats['max_loss']:.2f}")
        print(f"Average Holding Time: {stats['avg_holding_time_min']:.1f} minutes")
        print(f"Maximum Win Streak: {stats['max_win_streak']}")
        print(f"Maximum Loss Streak: {stats['max_loss_streak']}")
        
        # Monthly performance stats
        monthly = stats['monthly_stats']
        print("\nMONTHLY PERFORMANCE:")
        print(f"Average: {monthly['mean']:.2f}%")
        print(f"Median: {monthly['median']:.2f}%")
        print(f"Standard Deviation: {monthly['std']:.2f}%")
        print(f"Best Month: {monthly['best']:.2f}%")
        print(f"Worst Month: {monthly['worst']:.2f}%")
        
        # Calculate win rate by exit reason
        if self.results.trades:
            trade_df = pd.DataFrame(self.results.trades)
            
            print("\nEXIT REASON ANALYSIS:")
            reason_counts = pd.Series(stats['exit_reasons'])
            reason_pnl = trade_df.groupby('exit_reason')['pnl'].agg(['sum', 'mean', 'count'])
            
            for reason in reason_counts.index:
                wins = len(trade_df[(trade_df['exit_reason'] == reason) & (trade_df['pnl'] > 0)])
                total = reason_counts[reason]
                win_rate = wins / total if total > 0 else 0
                print(f"{reason}: {total} trades, Win Rate: {win_rate*100:.2f}%, Avg PnL: ${reason_pnl.loc[reason, 'mean']:.2f}")
        
        print("\n" + "="*80)

    def plot_results(self, figsize=(15, 12)):
        """Plot backtest results with price, indicators, and trade entries/exits"""
        if self.df is None or self.results is None:
            print("No data to plot. Run the backtest first.")
            return
        
        # Create figure with subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=figsize, gridspec_kw={'height_ratios': [3, 1, 1]})
        
        # Plot price data
        ax1.plot(self.df['timestamp'], self.df['close'], label='Price', color='black', alpha=0.7)
        
        # Plot strategy-specific indicators
        indicator_data = self.strategy.plot_indicators(self.df, ax1)
        
        # Plot trades
        if self.results.trades:
            trades_df = pd.DataFrame(self.results.trades)
            
            # Plot buy and sell entries
            buy_trades = trades_df[trades_df['side'] == 'buy']
            sell_trades = trades_df[trades_df['side'] == 'sell']
            
            if not buy_trades.empty:
                ax1.scatter(buy_trades['entry_time'], buy_trades['entry'], 
                           marker='^', color='green', s=100, label='Buy Entry')
                ax1.scatter(buy_trades['exit_time'], buy_trades['exit'], 
                           marker='x', color='red', s=100, label='Buy Exit')
                
            if not sell_trades.empty:
                ax1.scatter(sell_trades['entry_time'], sell_trades['entry'], 
                           marker='v', color='red', s=100, label='Sell Entry')
                ax1.scatter(sell_trades['exit_time'], sell_trades['exit'], 
                           marker='x', color='green', s=100, label='Sell Exit')
        
        # Format main chart
        ax1.set_title(f'{self.symbol} {self.timeframe} - Price Chart with {self.strategy.__class__.__name__}')
        ax1.set_ylabel('Price')
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc='upper left')
        
        # Plot secondary indicator (e.g., RSI, MACD)
        if indicator_data:
            ax2.plot(self.df['timestamp'], indicator_data['data'], 
                     label=indicator_data['label'], color=indicator_data['color'])
            
            # Add reference lines if provided
            if 'references' in indicator_data:
                for ref in indicator_data['references']:
                    ax2.axhline(y=ref['value'], color=ref['color'], 
                               linestyle='--', alpha=ref.get('alpha', 0.5))
            
            # Add overlay data if provided
            if 'overlay' in indicator_data:
                for overlay in indicator_data['overlay']:
                    if overlay.get('type') == 'bar':
                        ax2.bar(self.df['timestamp'], overlay['data'], 
                               color=overlay['color'], alpha=0.5, label=overlay['label'])
                    else:
                        ax2.plot(self.df['timestamp'], overlay['data'], 
                               color=overlay['color'], label=overlay['label'])
            
            ax2.set_title(indicator_data['title'])
            ax2.grid(True, alpha=0.3)
            ax2.legend(loc='upper left')
        
        # Plot equity curve
        if self.results.trades:
            # Calculate equity curve
            trades_df = pd.DataFrame(self.results.trades)
            trades_df['cumulative_pnl'] = trades_df['pnl'].cumsum()
            trades_df['equity'] = self.initial_capital + trades_df['cumulative_pnl']
            
            # Plot equity curve with date index
            ax3.plot(trades_df['exit_time'], trades_df['equity'], label='Equity Curve', color='blue')
            
            # Add drawdown shading
            if not trades_df.empty:
                peak = trades_df['equity'].expanding().max()
                drawdown = (trades_df['equity'] - peak) / peak * 100
                
                # Create a line at 0 for reference
                ax3.axhline(y=self.initial_capital, color='red', linestyle='--', alpha=0.3)
                
                # Annotate max drawdown
                max_dd_idx = drawdown.idxmin()
                if not pd.isna(max_dd_idx):
                    max_dd = drawdown.loc[max_dd_idx]
                    ax3.annotate(f'Max DD: {max_dd:.2f}%', 
                                xy=(trades_df['exit_time'].iloc[max_dd_idx], trades_df['equity'].iloc[max_dd_idx]),
                                xytext=(20, -30), textcoords='offset points',
                                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
            
            ax3.set_title('Equity Curve')
            ax3.set_ylabel('Account Value ($)')
            ax3.grid(True, alpha=0.3)
        
        # Format dates on x-axis
        for ax in [ax1, ax2, ax3]:
            ax.set_xlim(self.df['timestamp'].min(), self.df['timestamp'].max())
            
        fig.autofmt_xdate()
        plt.tight_layout()
        return fig


class OptimizeParams:
    """Class for optimizing strategy parameters"""
    
    def __init__(self, 
                 symbol, 
                 timeframe, 
                 strategy_class, 
                 param_ranges, 
                 risk_params=None,
                 initial_capital=20.0,
                 days_back=30,
                 data=None):
        
        self.symbol = symbol
        self.timeframe = timeframe
        self.strategy_class = strategy_class
        self.param_ranges = param_ranges
        self.risk_params = risk_params or {}
        self.initial_capital = initial_capital
        self.days_back = days_back
        self.data = data
        
        # Initialize results storage
        self.results = []
        
    def run(self, metric='total_profit_pct', n_top=5):
        """Run optimization across parameter combinations"""
        # Fetch data once for all tests
        if self.data is None:
            self.data = DataProvider.get_historical_data(self.symbol, self.timeframe, self.days_back)
            
        if self.data.empty:
            print("No data available for optimization.")
            return []
        
        # Generate parameter combinations
        param_names = list(self.param_ranges.keys())
        param_values = list(self.param_ranges.values())
        
        # Generate all combinations
        import itertools
        combinations = list(itertools.product(*param_values))
        
        print(f"Running optimization with {len(combinations)} parameter combinations...")
        
        # Create progress bar
        from tqdm import tqdm
        progress_bar = tqdm(total=len(combinations))
        
        # Test each combination
        for combo in combinations:
            # Create parameter dictionary
            params = dict(zip(param_names, combo))
            
            # Create strategy with these parameters
            strategy = self.strategy_class(params=params)
            
            # Create backtester
            risk_config = {
                'leverage': self.risk_params.get('leverage', 5.0),
                'risk_per_trade': self.risk_params.get('risk_per_trade', 0.01),
                'target_pct': self.risk_params.get('target_pct', 0.02),
                'stop_loss_pct': self.risk_params.get('stop_loss_pct', 0.01)
            }
            
            backtester = Backtester(
                symbol=self.symbol,
                timeframe=self.timeframe,
                strategy=strategy,
                initial_capital=self.initial_capital,
                leverage=risk_config['leverage'],
                risk_per_trade=risk_config['risk_per_trade'],
                target_pct=risk_config['target_pct'],
                stop_loss_pct=risk_config['stop_loss_pct']
            )
            
            # Run backtest
            results = backtester.run(data=self.data.copy())
            
            if results:
                stats = results.calculate_statistics()
                
                # Store results
                self.results.append({
                    'params': params,
                    'stats': stats,
                    'backtester': backtester
                })
            
            # Update progress bar
            progress_bar.update(1)
        
        # Close progress bar
        progress_bar.close()
        
        # Sort results by the specified metric
        sorted_results = sorted(self.results, key=lambda x: x['stats'].get(metric, 0), reverse=True)
        
        # Display top results
        self._display_top_results(sorted_results[:n_top], metric)
        
        return sorted_results[:n_top]
    
    def _display_top_results(self, top_results, metric):
        """Display top optimization results in a formatted table"""
        print("\n" + "="*100)
        print(f"TOP OPTIMIZATION RESULTS FOR {self.symbol} (Sorted by {metric})")
        print("="*100)
        
        # Table headers
        headers = ["Rank", "Parameters"]
        stats_to_show = ['total_profit_pct', 'win_rate', 'profit_factor', 
                         'max_drawdown_pct', 'total_trades', 'sharpe_ratio']
        
        headers.extend([s.replace('_', ' ').title() for s in stats_to_show])
        
        # Print headers
        header_str = "{:<5} {:<30} {:<15} {:<10} {:<15} {:<15} {:<15} {:<15}"
        print(header_str.format(*headers))
        print("-"*100)
        
        # Print each result
        for i, result in enumerate(top_results):
            params_str = ', '.join([f"{k}={v}" for k, v in result['params'].items()])
            
            # Format statistics
            stats_values = []
            for stat in stats_to_show:
                value = result['stats'].get(stat, 0)
                
                # Format based on stat type
                if 'pct' in stat or 'rate' in stat:
                    stats_values.append(f"{value:.2f}%")
                elif stat == 'total_trades':
                    stats_values.append(f"{int(value)}")
                else:
                    stats_values.append(f"{value:.2f}")
            
            # Build row
            row = [i+1, params_str] + stats_values
            print(header_str.format(*row))
        
        print("="*100)


class TradingCommand:
    """Command line interface for the trading system"""
    
    def __init__(self):
        """Initialize available strategies and commands"""
        self.available_strategies = {
            'maxrsi': MAXRSIStrategy,
            'ema': SimpleEMAStrategy
        }
        
        self.commands = {
            'backtest': self._run_backtest,
            'optimize': self._run_optimize,
            'help': self._show_help,
            'exit': self._exit
        }
        
        self.current_results = None
    
    def start(self):
        """Start the command line interface"""
        print("\n" + "="*60)
        print(" CRYPTO TRADING STRATEGY BACKTESTER ".center(60, "="))
        print("="*60)
        print("\nType 'help' for a list of commands.")
        
        running = True
        while running:
            command = input("\n> ").strip().lower()
            
            # Split command and arguments
            parts = command.split(' ')
            cmd = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            
            # Execute command if valid
            if cmd in self.commands:
                running = self.commands[cmd](args)
            else:
                print(f"Unknown command: {cmd}. Type 'help' for available commands.")
    
    def _run_backtest(self, args):
        """Run backtest with specified parameters"""
        if len(args) < 3:
            print("Usage: backtest <symbol> <timeframe> <strategy> [days_back] [risk_per_trade] [target_pct] [stop_loss_pct] [leverage]")
            print("Example: backtest BTCUSDT 1h maxrsi 30 0.01 0.02 0.01 5")
            return True
        
        # Parse arguments
        symbol = args[0].upper()
        timeframe = args[1].lower()
        strategy_name = args[2].lower()
        
        days_back = int(args[3]) if len(args) > 3 else 30
        risk_per_trade = float(args[4]) if len(args) > 4 else 0.01
        target_pct = float(args[5]) if len(args) > 5 else 0.02
        stop_loss_pct = float(args[6]) if len(args) > 6 else 0.01
        leverage = float(args[7]) if len(args) > 7 else 5.0
        
        # Check if strategy is valid
        if strategy_name not in self.available_strategies:
            print(f"Invalid strategy: {strategy_name}. Available strategies: {', '.join(self.available_strategies.keys())}")
            return True
        
        # Create strategy
        strategy_class = self.available_strategies[strategy_name]
        strategy = strategy_class()
        
        # Create backtester
        backtester = Backtester(
            symbol=symbol,
            timeframe=timeframe,
            strategy=strategy,
            initial_capital=20.0,
            leverage=leverage,
            risk_per_trade=risk_per_trade,
            target_pct=target_pct,
            stop_loss_pct=stop_loss_pct
        )
        
        print(f"\nRunning backtest for {symbol} on {timeframe} timeframe using {strategy_name.upper()} strategy...")
        print(f"Parameters: {days_back} days, Risk: {risk_per_trade*100}%, Target: {target_pct*100}%, Stop: {stop_loss_pct*100}%, Leverage: {leverage}x")
        
        # Run backtest
        results = backtester.run(days_back=days_back)
        
        if results:
            backtester.display_results()
            fig = backtester.plot_results()
            plt.show()
            
            # Store results for later reference
            self.current_results = backtester
        
        return True
    
    def _run_optimize(self, args):
        """Run parameter optimization"""
        if len(args) < 3:
            print("Usage: optimize <symbol> <timeframe> <strategy> [days_back]")
            print("Example: optimize BTCUSDT 1h maxrsi 30")
            return True
        
        # Parse arguments
        symbol = args[0].upper()
        timeframe = args[1].lower()
        strategy_name = args[2].lower()
        days_back = int(args[3]) if len(args) > 3 else 30
        
        # Check if strategy is valid
        if strategy_name not in self.available_strategies:
            print(f"Invalid strategy: {strategy_name}. Available strategies: {', '.join(self.available_strategies.keys())}")
            return True
        
        # Set parameter ranges based on strategy
        strategy_class = self.available_strategies[strategy_name]
        
        # Define parameter ranges based on strategy type
        param_ranges = {}
        if strategy_name == 'maxrsi':
            param_ranges = {
                'FAST_MA': [5, 9, 13],
                'SLOW_MA': [21, 34, 55],
                'RSI_PERIOD': [7, 14, 21],
                'RSI_MID': [45, 50, 55]
            }
        elif strategy_name == 'ema':
            param_ranges = {
                'FAST_EMA': [8, 12, 16],
                'SLOW_EMA': [21, 26, 34],
                'SIGNAL_EMA': [7, 9, 12]
            }
        
        # Set risk parameters
        risk_params = {
            'leverage': 5.0,
            'risk_per_trade': 0.01,
            'target_pct': 0.02, 
            'stop_loss_pct': 0.01
        }
        
        print(f"\nRunning optimization for {symbol} on {timeframe} timeframe using {strategy_name.upper()} strategy...")
        print(f"Looking back {days_back} days with {np.prod([len(v) for v in param_ranges.values()])} parameter combinations")
        
        # Create optimizer
        optimizer = OptimizeParams(
            symbol=symbol,
            timeframe=timeframe,
            strategy_class=strategy_class,
            param_ranges=param_ranges,
            risk_params=risk_params,
            days_back=days_back
        )
        
        # Run optimization
        top_results = optimizer.run(metric='sharpe_ratio')
        
        if top_results:
            # Store best result
            self.current_results = top_results[0]['backtester']
            
            # Plot best result
            fig = self.current_results.plot_results()
            plt.show()
        
        return True
    
    def _show_help(self, args):

        # The symbol should be XRPUSDT (without the slash)
        # The risk parameter should be a decimal (0.03 for 3%) rather than the whole number 3

        # Additionally, I'd recommend using more reasonable risk parameters. For example:

        # Risk per trade: 0.01 to 0.03 (1% to 3% of capital)
        # Target profit: 0.02 to 0.05 (2% to 5% profit target)
        # Stop loss: 0.01 to 0.02 (1% to 2% stop loss)


        """Show help information"""
        print("\nAvailable commands:")
        print("  backtest <symbol> <timeframe> <strategy> [days_back] [risk] [target] [stop] [leverage]")
        print("E.G. : backtest XRPUSDT 5m maxrsi 30 0.03 0.02 0.01 5")
        print("  optimize <symbol> <timeframe> <strategy> [days_back]")
        print("  help - Show this help message")
        print("  exit - Exit the program")
        print("\nAvailable strategies:")
        for name in self.available_strategies.keys():
            print(f"  {name}")
        print("\nTimeframe examples: 1m, 5m, 15m, 1h, 4h, 1d")
        return True
    
    def _exit(self, args):
        """Exit the program"""
        print("\nExiting...")
        return False


if __name__ == "__main__":
    cli = TradingCommand()
    cli.start()