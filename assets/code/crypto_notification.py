import requests
import time
from plyer import notification

class CryptoPriceAlert:
    def __init__(self, coin_symbol, limit_price, condition, notify_message):
        self.coin_symbol = coin_symbol.upper()
        self.limit_price = limit_price
        self.condition = condition.lower()  # 'above' or 'below'
        self.notify_message = notify_message
        self.coin_id = self._get_coin_id()

    def _get_coin_id(self):
        """Map symbol to CoinGecko API ID"""
        coin_map = {
            'BTC': 'bitcoin',
            'ETH': 'ethereum',
            'XRP': 'ripple',
            'LTC': 'litecoin'
        }
        return coin_map.get(self.coin_symbol, None)

    def check_price(self):
        """Get current price from CoinGecko API"""
        if not self.coin_id:
            print(f"Error: {self.coin_symbol} not supported")
            return None

        try:
            url = f"https://api.coingecko.com/api/v3/simple/price"
            params = {
                'ids': self.coin_id,
                'vs_currencies': 'usd'
            }
            response = requests.get(url, params=params)
            data = response.json()
            return data[self.coin_id]['usd']
        except Exception as e:
            print(f"Error fetching price: {str(e)}")
            return None

    def should_alert(self, current_price):
        """Check if price meets alert condition"""
        if current_price is None:
            return False
            
        if self.condition == 'above':
            return current_price > self.limit_price
        elif self.condition == 'below':
            return current_price < self.limit_price
        return False

def send_notification(title, message):
    """Show desktop notification"""
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='Crypto Alert',
            timeout=10
        )
    except Exception as e:
        print(f"Notification failed: {str(e)}")

def main():
    # Configure your alerts here
    alerts = [
        CryptoPriceAlert('BTC', 88800, 'above', 'BTC breaking $84k resistance!'),
        CryptoPriceAlert('XRP', 2.0912, 'below', 'XRP over long entry triggered!'),
        CryptoPriceAlert('BTC', 87000, 'below', 'BTC under support!')
    ]

    check_interval = 60  # Seconds between checks

    while True:
        try:
            for alert in alerts:
                price = alert.check_price()
                if price is not None and alert.should_alert(price):
                    message = f"{alert.coin_symbol} ${price:.2f} - {alert.notify_message}"
                    print(f"ALERT: {message}")
                    send_notification("Crypto Alert", message)
            
            time.sleep(check_interval)
            
        except KeyboardInterrupt:
            print("\nMonitoring stopped")
            break
        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(10)

if __name__ == "__main__":
    main()