import requests
import time
from datetime import datetime, timedelta
from colorama import Fore, Style, init

init(autoreset=True)

def get_order_book(symbol='XRPUSDT', limit=20):
    url = 'https://fapi.binance.com/fapi/v1/depth'
    params = {'symbol': symbol, 'limit': limit}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching order book: {e}")
        return None

def calculate_percentages(bids, asks):
    total_bids = sum(float(qty) for price, qty in bids)
    total_asks = sum(float(qty) for price, qty in asks)
    total = total_bids + total_asks
    buy_pct = (total_bids / total) * 100 if total != 0 else 0
    sell_pct = 100 - buy_pct
    return buy_pct, sell_pct, total_bids, total_asks

def get_color(pct, is_bid):
    if is_bid:
        if pct >= 20:
            return Fore.LIGHTGREEN_EX
        elif pct >= 10:
            return Fore.GREEN
        else:
            return Fore.LIGHTGREEN_EX
    else:
        if pct >= 20:
            return Fore.LIGHTRED_EX
        elif pct >= 10:
            return Fore.RED
        else:
            return Fore.LIGHTRED_EX

def main():
    history = []
    
    while True:
        data = get_order_book()
        if not data:
            time.sleep(2)
            continue
        
        current_time = datetime.now()
        
        # Process bids and asks
        bids = sorted([(float(price), float(qty)) for price, qty in data['bids']], key=lambda x: -x[0])
        asks = sorted([(float(price), float(qty)) for price, qty in data['asks']], key=lambda x: x[0])
        
        buy_pct, sell_pct, total_bids, total_asks = calculate_percentages(bids, asks)
        history.append((current_time, buy_pct, sell_pct))
        
        # Cleanup old history
        five_min_ago = current_time - timedelta(minutes=5)
        history = [entry for entry in history if entry[0] >= five_min_ago]
        
        # Calculate averages
        if history:
            avg_buy = sum(entry[1] for entry in history) / len(history)
            avg_sell = sum(entry[2] for entry in history) / len(history)
        else:
            avg_buy, avg_sell = 0, 0
        
        # Clear screen
        print("\033c", end="")
        
        # Print header
        print(f"\n{Fore.CYAN}=== XRPUSDT Futures Order Book ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Last Update: {current_time.strftime('%H:%M:%S')}{Style.RESET_ALL}")
        print(f"\n{Fore.WHITE}Bids{Style.RESET_ALL}{' ' * 25}{Fore.WHITE}Asks{Style.RESET_ALL}")
        
        # Print order book entries
        for i in range(5):
            bid_price, bid_qty = bids[i] if i < len(bids) else (0, 0)
            ask_price, ask_qty = asks[i] if i < len(asks) else (0, 0)
            
            # Calculate percentages
            bid_pct = (bid_qty / total_bids * 100) if total_bids != 0 else 0
            ask_pct = (ask_qty / total_asks * 100) if total_asks != 0 else 0
            
            # Get colors
            bid_color = get_color(bid_pct, True)
            ask_color = get_color(ask_pct, False)
            
            # Format output
            bid_str = f"{bid_color}{bid_price:8.4f} {bid_qty:8.1f} {bid_pct:5.1f}%{Style.RESET_ALL}"
            ask_str = f"{ask_color}{ask_price:8.4f} {ask_qty:8.1f} {ask_pct:5.1f}%{Style.RESET_ALL}"
            print(f"{bid_str} | {ask_str}")
        
        # Print summary
        print(f"\n{Fore.CYAN}Current Buy/Sell Ratio:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Buy: {buy_pct:.1f}%{Style.RESET_ALL}  {Fore.RED}Sell: {sell_pct:.1f}%{Style.RESET_ALL}")
        print(f"{Fore.CYAN}5-Minute Average:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Buy: {avg_buy:.1f}%{Style.RESET_ALL}  {Fore.RED}Sell: {avg_sell:.1f}%{Style.RESET_ALL}")
        
        # Refresh every 2 seconds
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Script terminated by user.{Style.RESET_ALL}")