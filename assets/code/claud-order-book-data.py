import requests
import pandas as pd
import time
import os
from datetime import datetime, timedelta
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class OrderBookMonitor:
    def __init__(self, symbol='XRPUSDT', depth=10):
        self.symbol = symbol
        self.depth = depth
        self.base_url = "https://fapi.binance.com"
        self.historical_ratios = []
        self.last_5min_ratios = []
        self.start_time = datetime.now()

    def fetch_order_book(self):
        """Fetch order book data directly from Binance API"""
        try:
            endpoint = f"/fapi/v1/depth"
            params = {
                'symbol': self.symbol,
                'limit': self.depth
            }
            response = requests.get(self.base_url + endpoint, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
            
            data = response.json()
            orderbook = {
                'bids': [[float(price), float(qty)] for price, qty in data['bids']],
                'asks': [[float(price), float(qty)] for price, qty in data['asks']]
            }
            return orderbook
        except Exception as e:
            print(f"{Fore.RED}Error fetching orderbook: {e}{Style.RESET_ALL}")
            return None

    def calculate_buy_sell_ratio(self, orderbook):
        """Calculate buy/sell ratio from orderbook data"""
        if not orderbook:
            return None, None, None

        bids = orderbook['bids']  # Buy orders
        asks = orderbook['asks']  # Sell orders
        
        # Calculate total volume and notional value for bids and asks
        bid_volume = sum(bid[1] for bid in bids)
        ask_volume = sum(ask[1] for ask in asks)
        
        bid_value = sum(bid[0] * bid[1] for bid in bids)
        ask_value = sum(ask[0] * ask[1] for ask in asks)
        
        # Calculate buy/sell ratios
        volume_ratio = (bid_volume / ask_volume) if ask_volume else float('inf')
        value_ratio = (bid_value / ask_value) if ask_value else float('inf')
        
        # Calculate buy percentage
        buy_percentage = (bid_volume / (bid_volume + ask_volume)) * 100 if (bid_volume + ask_volume) else 50
        
        return volume_ratio, value_ratio, buy_percentage

    def update_historical_data(self, buy_percentage):
        """Update historical buy percentage data"""
        current_time = datetime.now()
        self.historical_ratios.append((current_time, buy_percentage))
        
        # Keep only data from the last 5 minutes
        cutoff_time = current_time - timedelta(minutes=5)
        self.last_5min_ratios = [(t, r) for t, r in self.historical_ratios if t >= cutoff_time]

    def calculate_average_percentage(self):
        """Calculate average buy percentage for the last 5 minutes"""
        if not self.last_5min_ratios:
            return None
        
        avg_percentage = sum(r for _, r in self.last_5min_ratios) / len(self.last_5min_ratios)
        return avg_percentage

    def display_order_book(self, orderbook, buy_percentage, avg_percentage):
        """Display order book with colors and percentages"""
        if not orderbook:
            return
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"\n{Fore.YELLOW}==== {self.symbol} Order Book ===={Style.RESET_ALL}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Display buy percentage with color based on value
        color = Fore.GREEN if buy_percentage > 50 else Fore.RED
        print(f"\nCurrent Buy %: {color}{buy_percentage:.2f}%{Style.RESET_ALL}")
        print(f"Current Sell %: {Fore.RED if buy_percentage < 50 else Fore.GREEN}{100 - buy_percentage:.2f}%{Style.RESET_ALL}")
        
        # Display average buy percentage for last 5 minutes
        if avg_percentage is not None:
            avg_color = Fore.GREEN if avg_percentage > 50 else Fore.RED
            print(f"Average Buy % (5min): {avg_color}{avg_percentage:.2f}%{Style.RESET_ALL}")
            print(f"Average Sell % (5min): {Fore.RED if avg_percentage > 50 else Fore.GREEN}{100 - avg_percentage:.2f}%{Style.RESET_ALL}")
        else:
            print("Average Buy % (5min): Not enough data")
        
        # Display sell orders (asks)
        print(f"\n{Fore.RED}===== SELL ORDERS ====={Style.RESET_ALL}")
        for price, volume in reversed(orderbook['asks']):
            value = price * volume
            print(f"{Fore.RED}Price: {price:.5f} | Volume: {volume:.2f} | Value: ${value:.2f}{Style.RESET_ALL}")
        
        # Display spread
        if orderbook['bids'] and orderbook['asks']:
            best_bid = orderbook['bids'][0][0]
            best_ask = orderbook['asks'][0][0]
            spread = best_ask - best_bid
            spread_pct = (spread / best_bid) * 100
            print(f"\n{Fore.YELLOW}Spread: ${spread:.5f} ({spread_pct:.3f}%){Style.RESET_ALL}")
        
        # Display buy orders (bids)
        print(f"\n{Fore.GREEN}===== BUY ORDERS ====={Style.RESET_ALL}")
        for price, volume in orderbook['bids']:
            value = price * volume
            print(f"{Fore.GREEN}Price: {price:.5f} | Volume: {volume:.2f} | Value: ${value:.2f}{Style.RESET_ALL}")

    def run(self, refresh_rate=1):
        """Main monitoring loop"""
        print(f"Starting Order Book Monitor for {self.symbol}...")
        print("Press Ctrl+C to exit")
        
        try:
            while True:
                orderbook = self.fetch_order_book()
                if orderbook:
                    _, _, buy_percentage = self.calculate_buy_sell_ratio(orderbook)
                    self.update_historical_data(buy_percentage)
                    avg_percentage = self.calculate_average_percentage()
                    self.display_order_book(orderbook, buy_percentage, avg_percentage)
                
                time.sleep(refresh_rate)
                
        except KeyboardInterrupt:
            print("\nExiting Order Book Monitor...")

if __name__ == "__main__":
    # Create and run the order book monitor
    monitor = OrderBookMonitor(symbol='XRPUSDT', depth=10)
    monitor.run(refresh_rate=2)  # Update every 2 seconds