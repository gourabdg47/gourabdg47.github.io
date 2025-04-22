import requests
import time
import numpy as np
from datetime import datetime, timedelta
from collections import deque
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Configuration
SYMBOL = 'XRPUSDT'
DEPTH_LEVELS = 100
REFRESH_INTERVAL = 2  # seconds
HISTORY_MINUTES = 5
CLUSTER_INTERVAL = 0.0005
ORDER_BOOK_HISTORY_SIZE = 8

def get_current_price():
    url = 'https://fapi.binance.com/fapi/v1/ticker/price'
    try:
        response = requests.get(url, params={'symbol': SYMBOL})
        return float(response.json()['price'])
    except Exception as e:
        print(f"Error getting price: {e}")
        return None

def get_order_book():
    url = 'https://fapi.binance.com/fapi/v1/depth'
    try:
        response = requests.get(url, params={'symbol': SYMBOL, 'limit': DEPTH_LEVELS})
        return response.json()
    except Exception as e:
        print(f"Error getting order book: {e}")
        return None


def generate_signals(metrics):
    """Generate scalping signals based on market conditions"""
    current_price = metrics['current_price']
    trend = metrics['trend']
    support = [p for p, _ in metrics['support']]
    resistance = [p for p, _ in metrics['resistance']]
    
    # Signal logic
    signal = "Hold"
    target = stop_loss = entry = leverage = timeframe = win_pct = 0
    
    # Calculate volatility-adjusted targets
    volatility_factor = max(0.0005, metrics['volatility'] / 100)
    base_target = current_price * volatility_factor * 2
    base_stop = current_price * volatility_factor
    
    # Trend-based signals
    if "uptrend" in trend.lower() and current_price > np.mean(support[:2]):
        signal = "Long"
        target = current_price + base_target
        stop_loss = current_price - base_stop
        win_pct = min(90, 60 + metrics['buy_pct'] * 0.4)
    elif "downtrend" in trend.lower() and current_price < np.mean(resistance[:2]):
        signal = "Short"
        target = current_price - base_target
        stop_loss = current_price + base_stop
        win_pct = min(90, 60 + metrics['sell_pct'] * 0.4)
    
    # Leverage calculation based on volatility
    leverage = max(1, min(10, int(3 / (metrics['volatility'] + 0.1))))
    
    # Entry price and timeframe
    entry = current_price
    timeframe = "5min"
    
    # Liquidity sweep detection
    if metrics['price_momentum'] > 50 and signal == "Long":
        win_pct += 5
    elif metrics['price_momentum'] < -50 and signal == "Short":
        win_pct += 5
    
    return {
        'signal': signal,
        'target': target,
        'stop_loss': stop_loss,
        'entry': entry,
        'leverage': leverage,
        'timeframe': timeframe,
        'win_pct': min(95, max(50, win_pct))
    }


def calculate_metrics(bids, asks, current_price):
    bids = np.array(sorted([(float(p), float(q)) for p, q in bids], reverse=True))
    asks = np.array(sorted([(float(p), float(q)) for p, q in asks]))
    
    total_bids = bids[:,1].sum()
    total_asks = asks[:,1].sum()
    total_liquidity = total_bids + total_asks
    
    buy_pct = (total_bids / total_liquidity) * 100
    sell_pct = 100 - buy_pct
    bs_ratio = total_bids / total_asks if total_asks != 0 else 1
    
    spread = asks[0][0] - bids[0][0]
    volatility = (spread / current_price) * 100
    
    bid_vwap = np.sum(bids[:,0] * bids[:,1]) / total_bids if total_bids != 0 else current_price
    ask_vwap = np.sum(asks[:,0] * asks[:,1]) / total_asks if total_asks != 0 else current_price
    price_momentum = (bid_vwap - ask_vwap) / ((bid_vwap + ask_vwap)/2) * 10000
    
    if price_momentum > 50:
        trend = "Strong uptrend ▲▲"
    elif price_momentum > 20:
        trend = "Uptrend ▲"
    elif price_momentum < -50:
        trend = "Strong downtrend ▼▼"
    elif price_momentum < -20:
        trend = "Downtrend ▼"
    else:
        trend = "Neutral ➔"
    
    def get_clusters(side):
        clusters = {}
        for price, qty in side:
            cluster = round(price / CLUSTER_INTERVAL) * CLUSTER_INTERVAL
            clusters[cluster] = clusters.get(cluster, 0) + qty
        return sorted(clusters.items(), key=lambda x: x[1], reverse=True)
    
    bid_clusters = get_clusters(bids)
    ask_clusters = get_clusters(asks)
    
    support = [(p, v) for p, v in bid_clusters if p < current_price][:3]
    resistance = [(p, v) for p, v in ask_clusters if p > current_price][:3]
    
    return {
        'current_price': current_price,
        'buy_pct': buy_pct,
        'sell_pct': sell_pct,
        'bs_ratio': bs_ratio,
        'volatility': volatility,
        'total_liquidity': total_liquidity,
        'liquidity_ratio': total_bids / total_asks,
        'support': support,
        'resistance': resistance,
        'trend': trend,
        'price_momentum': price_momentum,
        'market_pressure': "Strong selling pressure" if sell_pct > 55 else 
                         "Moderate selling pressure" if sell_pct > 51 else
                         "Strong buying pressure" if buy_pct > 55 else
                         "Moderate buying pressure" if buy_pct > 51 else
                         "Balanced market",
        'timestamp': datetime.now()
    }

def main():
    history = []
    recent_order_books = deque(maxlen=ORDER_BOOK_HISTORY_SIZE)
    signal_history = deque(maxlen=10)

    while True:
        current_price = get_current_price()
        order_book = get_order_book()
        
        if not current_price or not order_book:
            time.sleep(REFRESH_INTERVAL)
            continue
        
        metrics = calculate_metrics(order_book['bids'], order_book['asks'], current_price)
        recent_order_books.appendleft(metrics)
        signals = generate_signals(metrics)
        signal_history.append(signals)
        
        # Update history for averages
        history.append((metrics['timestamp'], metrics['buy_pct'], metrics['sell_pct']))
        cutoff_time = datetime.now() - timedelta(minutes=HISTORY_MINUTES)
        history = [h for h in history if h[0] > cutoff_time]
        
        # Calculate averages
        buy_history = [h[1] for h in history]
        sell_history = [h[2] for h in history]
        avg_buy = np.mean(buy_history) if buy_history else 0
        avg_sell = np.mean(sell_history) if sell_history else 0
        
        # Clear screen
        print("\033c", end="")
        
        # Display header
        print(f"\n{Fore.CYAN}=== REAL-TIME {SYMBOL} FUTURES ANALYSIS ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Last Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")

        # Scalping Signals Section
        print(f"\n{Fore.MAGENTA}SCALPING SIGNALS (5min timeframe):{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'Direction':<8} | {'Entry':<10} | {'Target':<10} | {'Stop Loss':<10} | {'Leverage':<8} | {'Win %':<6}")
        print("-" * 70)
        
        signal_color = Fore.GREEN if signals['signal'] == "Long" else Fore.RED if signals['signal'] == "Short" else Fore.YELLOW
        leverage_color = Fore.RED if signals['leverage'] > 5 else Fore.YELLOW if signals['leverage'] > 3 else Fore.GREEN
        
        print(f"{signal_color}{signals['signal']:<8}{Style.RESET_ALL} | "
              f"{Fore.WHITE}{signals['entry']:.5f} | "
              f"{Fore.GREEN}{signals['target']:.5f} | "
              f"{Fore.RED}{signals['stop_loss']:.5f} | "
              f"{leverage_color}{signals['leverage']:<8}x{Style.RESET_ALL} | "
              f"{Fore.CYAN}{signals['win_pct']:.1f}%")

        # Order Book History
        print(f"\n{Fore.MAGENTA}LAST {ORDER_BOOK_HISTORY_SIZE} ORDER BOOK UPDATES:")
        print(f"{Fore.WHITE}{'Time':<10} | {'Buy %':<8} | {'Sell %':<8} | {'Status':<12}")
        print("-" * 45)
        for entry in recent_order_books:
            time_str = entry['timestamp'].strftime("%H:%M:%S")
            buy_color = Fore.GREEN if entry['buy_pct'] > 50 else Fore.YELLOW
            sell_color = Fore.RED if entry['sell_pct'] > 50 else Fore.YELLOW
            print(f"{Fore.WHITE}{time_str:<10} | "
                  f"{buy_color}{entry['buy_pct']:6.2f}% {Style.RESET_ALL}| "
                  f"{sell_color}{entry['sell_pct']:6.2f}% {Style.RESET_ALL}| "
                  f"{Fore.CYAN}{entry['market_pressure']}")

        # Price & Market Info
        print(f"\n{Fore.MAGENTA}CURRENT MARKET SNAPSHOT:")
        print(f"{Fore.WHITE}Price: {Fore.GREEN}${metrics['current_price']:.5f}  "
              f"Buy/Sell Ratio: {Fore.CYAN}{metrics['bs_ratio']:.2f}")
        print(f"Current Buy: {Fore.GREEN}{metrics['buy_pct']:.2f}%  "
              f"Sell: {Fore.RED}{metrics['sell_pct']:.2f}%")
        print(f"5min Avg Buy: {Fore.CYAN}{avg_buy:.2f}%  "
              f"Avg Sell: {Fore.CYAN}{avg_sell:.2f}%")

        # Market Analysis
        print(f"\n{Fore.MAGENTA}MARKET ANALYSIS:")
        trend_color = Fore.GREEN if 'up' in metrics['trend'].lower() else Fore.RED if 'down' in metrics['trend'].lower() else Fore.YELLOW
        print(f"Trend: {trend_color}{metrics['trend']}  "
              f"Pressure: {Fore.RED if 'sell' in metrics['market_pressure'] else Fore.GREEN}{metrics['market_pressure']}")
        print(f"Volatility: {Fore.WHITE}{metrics['volatility']:.4f}%  "
              f"Momentum: {Fore.CYAN}{metrics['price_momentum']:+.2f} bps")

        # Liquidity & Levels
        print(f"\n{Fore.MAGENTA}LIQUIDITY ANALYSIS:")
        print(f"Total: {Fore.WHITE}{metrics['total_liquidity']:,.2f}  "
              f"Ratio: {Fore.CYAN}{metrics['liquidity_ratio']:.2f}")
        print(f"{Fore.GREEN}Support Levels:{Style.RESET_ALL}")
        for p, v in metrics['support']:
            print(f"  ${p:.5f} - {Fore.WHITE}{v:,.2f}")
        print(f"{Fore.RED}Resistance Levels:{Style.RESET_ALL}")
        for p, v in metrics['resistance']:
            print(f"  ${p:.5f} - {Fore.WHITE}{v:,.2f}")

        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Analysis terminated.{Style.RESET_ALL}")
