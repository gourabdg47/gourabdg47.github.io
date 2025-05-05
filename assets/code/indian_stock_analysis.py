# -*- coding: utf-8 -*-
"""
Stock Analysis Script (v2 - Fixed Issues)

Fetches data for a given Indian stock symbol, displays technical analysis,
key metrics, news, sentiment, momentum, and basic price trend predictions.

Fixes:
- Corrected Dividend Yield calculation.
- Addressed scikit-learn UserWarnings related to feature names.
- Ensured color coding applies correctly in the output table.

Disclaimer: This script is for informational and educational purposes only.
It does not constitute financial advice. Stock market investments involve risk.
Predictions are based on simple models and historical data, and are highly
speculative and likely inaccurate. Always conduct thorough research and consult
a qualified financial advisor before trading or investing. Data may be delayed.
"""

import yfinance as yf
import pandas as pd
import numpy as np
import pandas_ta as ta
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta
import warnings

# --- Rich for enhanced console output ---
try:
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    print("Rich library not found. Output will be plain text.")
    print("Install rich: pip install rich")
    RICH_AVAILABLE = False

    # Define dummy functions if rich is not available
    class DummyConsole:
        def print(self, *args, **kwargs):
            # Basic color emulation for plain text
            style = kwargs.get('style', '')
            text = " ".join(map(str, args))
            if 'bold red' in style:
                print(f"ERROR: {text}")
            elif 'red' in style:
                 print(f"ALERT: {text}")
            elif 'yellow' in style:
                 print(f"WARN: {text}")
            elif 'green' in style:
                 print(f"OK: {text}")
            elif 'cyan' in style:
                 print(f"INFO: {text}")
            else:
                print(text)

    console = DummyConsole()
    # Use a simple class wrapper for Text in plain mode
    class PlainText:
        def __init__(self, text, style=None):
            prefix = ""
            if style == "green": prefix = "[OK] "
            elif style == "red": prefix = "[ALERT] "
            elif style == "yellow": prefix = "[WARN] "
            self.text = prefix + str(text)
        def __str__(self):
            return self.text
    Text = PlainText

# --- Helper Functions ---

def format_value(value, precision=2):
    """Formats numbers, handling None values."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "N/A"
    try:
        if abs(value) >= 1e7:  # Crores (10 million)
            return f"₹{value / 1e7:.{precision}f} Cr"
        if abs(value) >= 1e5:  # Lakhs (100 thousand)
            return f"₹{value / 1e5:.{precision}f} L"
        if isinstance(value, (int, float)):
             # Format as percentage if it's likely a yield/small decimal
             if abs(value) < 1 and precision > 0:
                  return f"{value * 100:.{precision}f}%"
             return f"{value:.{precision}f}" # Format as regular number
        return str(value)
    except TypeError:
        return str(value) # Return as string if formatting fails

def format_yield(value, precision=2):
     """Formats yield specifically as percentage."""
     if value is None or (isinstance(value, float) and np.isnan(value)):
        return "N/A"
     return f"{value * 100:.{precision}f}%"


def get_color(value=None, positive_is_good=True, neutral_threshold=0.05, is_percent=False):
    """Returns color coding for rich Text."""
    default_color = "white"
    if not RICH_AVAILABLE or value is None or isinstance(value, str) or np.isnan(value):
        return default_color

    # Adjust threshold if comparing percentages directly
    threshold = neutral_threshold / 100.0 if is_percent else neutral_threshold

    try:
        numeric_value = float(value)
        if positive_is_good:
            if numeric_value > threshold: return "green"
            elif numeric_value < -threshold: return "red"
            else: return "yellow"
        else: # Negative is good (e.g., PE ratio lower is better sometimes - though color usually not applied here)
             if numeric_value < -threshold: return "green"
             elif numeric_value > threshold: return "red"
             else: return "yellow"
    except (ValueError, TypeError):
        return default_color # Return default if value is not numeric

def get_rsi_color(rsi_value):
    """Color for RSI."""
    if not RICH_AVAILABLE or rsi_value is None or np.isnan(rsi_value):
        return "white"
    if rsi_value > 70:
        return "red" # Overbought
    elif rsi_value < 30:
        return "green" # Oversold
    else:
        return "yellow" # Neutral

def get_macd_color(macd_line, signal_line):
    """Color for MACD based on crossover."""
    if not RICH_AVAILABLE or macd_line is None or signal_line is None or np.isnan(macd_line) or np.isnan(signal_line):
        return "white"
    if macd_line > signal_line:
        return "green" # Bullish crossover
    else:
        return "red" # Bearish crossover

def get_price_ma_color(price, ma_value):
    """Color based on price vs Moving Average."""
    if not RICH_AVAILABLE or price is None or ma_value is None or np.isnan(price) or np.isnan(ma_value):
        return "white"
    if price > ma_value:
        return "green" # Above MA (Bullish short-term context)
    else:
        return "red" # Below MA (Bearish short-term context)

# --- Main Analysis Function ---

def analyze_stock(symbol):
    """Performs analysis for the given stock symbol."""
    try:
        console.print(f"\nFetching data for [bold cyan]{symbol}[/bold cyan]...", style="italic yellow")
        ticker = yf.Ticker(symbol)

        # 1. Fetch Basic Info & Historical Data
        # Use info first as it contains pre-calculated yield etc.
        info = ticker.info
        hist_1y = ticker.history(period="1y")
        hist_3y = ticker.history(period="3y") # For regression

        if hist_1y.empty:
            console.print(f"Could not fetch historical data for {symbol}. Invalid symbol or no data?", style="bold red")
            return

        # Ensure we have necessary info dictionary keys
        if not info or not info.get('regularMarketPreviousClose'):
             # Fallback if info is empty or lacks essential keys
             last_close = hist_1y['Close'].iloc[-1]
             prev_close = hist_1y['Close'].iloc[-2] if len(hist_1y) > 1 else last_close
             current_price = info.get('currentPrice', last_close) # Use currentPrice if available
        else:
            # Prefer info dict values if available and seem valid
            current_price = info.get('currentPrice', hist_1y['Close'].iloc[-1]) # Use live price if possible
            last_close = info.get('regularMarketPrice', current_price) # Use regularMarketPrice if possible
            prev_close = info.get('regularMarketPreviousClose')

        price_change = last_close - prev_close
        price_change_pct = (price_change / prev_close) * 100 if prev_close else 0

        # 2. Extract Key Info (with checks)
        stock_name = info.get('longName', symbol)
        currency = info.get('currency', 'INR')
        market_cap = info.get('marketCap')
        pe_ratio = info.get('trailingPE')
        pb_ratio = info.get('priceToBook')
        beta = info.get('beta') # Measure of volatility vs market
        volume = info.get('regularMarketVolume', hist_1y['Volume'].iloc[-1]) # Prefer info volume
        high_52wk = info.get('fiftyTwoWeekHigh')
        low_52wk = info.get('fiftyTwoWeekLow')

        # --- Dividend Yield Correction ---
        dividend_yield_raw = info.get('dividendYield') # This is usually the decimal value
        dividend_rate = info.get('dividendRate') # Annual dividend amount per share

        if dividend_yield_raw is not None and 0 < dividend_yield_raw < 0.20: # Check if yield is reasonable (0-20%)
            dividend_yield = dividend_yield_raw
        elif dividend_rate is not None and prev_close is not None and prev_close > 0:
            # Try calculating manually if yield seems off or missing
            dividend_yield = dividend_rate / prev_close
            console.print(f"Note: Dividend Yield calculated manually ({dividend_rate} / {prev_close}).", style="italic dim")
        else:
            dividend_yield = 0 # Assume zero if no data

        console.print(f"\n--- [bold magenta]{stock_name} ({symbol})[/bold magenta] ---", style="underline")
        price_color = get_color(price_change) if RICH_AVAILABLE else 'white'
        console.print(f"Last Price: {format_value(last_close)} ({format_value(price_change)} / {price_change_pct:.2f}%)", style=price_color)
        console.print(f"52 Week Range: {format_value(low_52wk)} - {format_value(high_52wk)}")

        # 3. Dividend, Sentiment, Momentum, News (Partially pre-filled for IGL.NS based on context)
        console.print(f"\nDividend Yield: {format_yield(dividend_yield)}", style="blue") # Use specific yield formatter

        # --- Sentiment & Momentum (Example for IGL.NS - Needs real source otherwise) ---
        sentiment = "N/A"
        sentiment_text_obj = Text("N/A") # Default
        momentum = "N/A"
        momentum_text_obj = Text("N/A") # Default

        if symbol == "IGL.NS":
            sentiment = "Neutral to Positive"
            sentiment_color = "yellow" # Mix of buy ratings and concerns
            sentiment_text_obj = Text(sentiment, style=sentiment_color)

            momentum = "Mixed (Short-Term Positive, Long-Term Negative)"
            momentum_color = "yellow"
            momentum_text_obj = Text(momentum, style=momentum_color)

            news_headlines = [
                "Indraprastha Gas Appoints New Chairman (May 2025)",
                "IGL Explores Entry into LNG Retail Sales (May 2025)",
                "IGL Reports Improved Q4 Financial Performance (Apr/May 2025)",
                "IGL share price up 8% in 2 days after Q4 results (Apr 2025)",
                "Kotak Securities cautious on city gas firms as EVs rise (Apr 2025)"
            ]
        else:
            # Generic placeholders - replace with actual fetch/analysis if possible
            sentiment = "Data Unavailable" # Placeholder
            sentiment_text_obj = Text(sentiment)

            # Infer momentum from recent returns or technicals
            mom_1m_ret = hist_1y['Close'].pct_change(periods=20).iloc[-1]
            if not pd.isna(mom_1m_ret):
                momentum = f"1M Return: {mom_1m_ret:.2%}"
                momentum_color = get_color(mom_1m_ret, is_percent=False) # Compare raw decimal return
                momentum_text_obj = Text(momentum, style=momentum_color)
            else:
                 momentum_text_obj = Text("N/A")

            # Fetch news using yfinance
            try:
                news = ticker.news
                if news:
                     news_headlines = [f"{item['title']} (Source: {item.get('publisher', 'N/A')})" for item in news[:5]] # Get top 5
                else:
                     news_headlines = ["No recent news found via yfinance."]
            except Exception as e:
                news_headlines = [f"Could not fetch news: {e}"]


        console.print(f"Market Sentiment: ", sentiment_text_obj)
        console.print(f"Momentum Status: ", momentum_text_obj)

        console.print("\n[bold]Latest News Headlines:[/bold]")
        if news_headlines:
            for i, headline in enumerate(news_headlines):
                console.print(f"{i+1}. {headline}")
        else:
            console.print("No recent news found.")

        # 4. Calculate Technical Indicators
        console.print("\nCalculating Technical Indicators...", style="italic yellow")
        df = hist_1y.copy().tail(250) # Use ~1 year of data, ensure enough length
        if len(df) > 20: df.ta.sma(length=20, append=True)
        if len(df) > 50: df.ta.sma(length=50, append=True)
        if len(df) > 200: df.ta.sma(length=200, append=True)
        if len(df) > 14: df.ta.rsi(length=14, append=True)
        if len(df) > 30: df.ta.macd(fast=12, slow=26, signal=9, append=True) # Appends MACD_12_26_9, MACDh_12_26_9, MACDs_12_26_9

        # Get latest values safely
        latest_data = df.iloc[-1] if not df.empty else pd.Series()
        sma_20 = latest_data.get('SMA_20')
        sma_50 = latest_data.get('SMA_50')
        sma_200 = latest_data.get('SMA_200')
        rsi_14 = latest_data.get('RSI_14')
        macd_line = latest_data.get('MACD_12_26_9')
        macd_signal = latest_data.get('MACDs_12_26_9')
        macd_hist = latest_data.get('MACDh_12_26_9')

        # 5. Display Table using Rich
        if RICH_AVAILABLE:
            table = Table(title="\nStock Analysis Summary", show_header=True, header_style="bold magenta")
            table.add_column("Metric", style="cyan", width=25)
            table.add_column("Value", style="bold")
            table.add_column("Signal/Status", style="bold")

            # --- Key Metrics ---
            table.add_row("Market Cap", format_value(market_cap), "")
            table.add_row("Volume (Last Session)", format_value(volume,0), "")
            table.add_row("P/E Ratio (TTM)", format_value(pe_ratio), Text("Lower can be better", style="italic dim"))
            table.add_row("P/B Ratio", format_value(pb_ratio), Text("Lower can be better", style="italic dim"))
            table.add_row("Beta", format_value(beta), Text(">1 More Volatile", style="italic dim"))

            # --- Technical Indicators ---
            table.add_section()
            price_vs_sma20_status = "Above" if last_close > sma_20 else "Below" if sma_20 is not None else "N/A"
            price_vs_sma20_color = get_price_ma_color(last_close, sma_20)
            table.add_row("Price vs SMA(20)", f"{format_value(last_close)} vs {format_value(sma_20)}", Text(price_vs_sma20_status, style=price_vs_sma20_color))

            price_vs_sma50_status = "Above" if last_close > sma_50 else "Below" if sma_50 is not None else "N/A"
            price_vs_sma50_color = get_price_ma_color(last_close, sma_50)
            table.add_row("Price vs SMA(50)", f"{format_value(last_close)} vs {format_value(sma_50)}", Text(price_vs_sma50_status, style=price_vs_sma50_color))

            price_vs_sma200_status = "Above" if last_close > sma_200 else "Below" if sma_200 is not None else "N/A"
            price_vs_sma200_color = get_price_ma_color(last_close, sma_200)
            table.add_row("Price vs SMA(200)", f"{format_value(last_close)} vs {format_value(sma_200)}", Text(price_vs_sma200_status, style=price_vs_sma200_color))

            rsi_color = get_rsi_color(rsi_14)
            rsi_status = "Overbought" if rsi_color == "red" else "Oversold" if rsi_color == "green" else "Neutral" if rsi_color == "yellow" else "N/A"
            table.add_row("RSI(14)", format_value(rsi_14), Text(rsi_status, style=rsi_color))

            macd_color = get_macd_color(macd_line, macd_signal)
            macd_status = "Bullish" if macd_color == "green" else "Bearish" if macd_color == "red" else "N/A"
            table.add_row("MACD(12,26,9)", f"L:{format_value(macd_line)} S:{format_value(macd_signal)} H:{format_value(macd_hist)}", Text(macd_status, style=macd_color))

            console.print(table)
        else:
            # Plain text fallback
            print("\n--- Key Metrics ---")
            print(f"Market Cap: {format_value(market_cap)}")
            print(f"Volume: {format_value(volume, 0)}")
            print(f"P/E Ratio: {format_value(pe_ratio)}")
            print(f"P/B Ratio: {format_value(pb_ratio)}")
            print(f"Beta: {format_value(beta)}")
            print("\n--- Technical Indicators (Latest) ---")
            print(f"SMA(20): {format_value(sma_20)}")
            print(f"SMA(50): {format_value(sma_50)}")
            print(f"SMA(200): {format_value(sma_200)}")
            print(f"RSI(14): {format_value(rsi_14)}")
            print(f"MACD Line: {format_value(macd_line)}")
            print(f"MACD Signal: {format_value(macd_signal)}")
            print(f"MACD Hist: {format_value(macd_hist)}")


        # 6. Predictive Modeling (Basic & Speculative)
        console.print("\n--- Predictive Modeling (Highly Speculative) ---", style="underline bold red")
        if hist_3y.empty or len(hist_3y) < 60: # Need sufficient data
             console.print("Not enough historical data for predictive modeling.", style="yellow")
             return

        # --- Linear Regression for Trend ---
        console.print("\n[bold]Linear Regression Trend (Next 12 Weeks):[/bold]")
        lr_df = hist_3y[['Close']].copy()
        lr_df = lr_df.dropna() # Ensure no NaNs in Close price
        lr_df['Days'] = (lr_df.index - lr_df.index.min()).days
        X_lr = lr_df[['Days']]
        y_lr = lr_df['Close']

        if len(X_lr) < 2:
            console.print("Not enough data points for Linear Regression.", style="yellow")
        else:
            model_lr = LinearRegression()
            model_lr.fit(X_lr, y_lr)

            # Predict 12 weeks (84 days) from the last historical day
            last_day_num = lr_df['Days'].iloc[-1]
            future_days = np.array(range(last_day_num + 1, last_day_num + 84 + 1)).reshape(-1, 1)
            # Convert prediction input to DataFrame with feature name to avoid warning
            future_days_df = pd.DataFrame(future_days, columns=['Days'])
            future_preds_lr = model_lr.predict(future_days_df)

            predicted_price_12w = future_preds_lr[-1]
            trend_direction = "Upward" if predicted_price_12w > last_close else "Downward"
            trend_color = "green" if trend_direction == "Upward" else "red"

            console.print(f"Based purely on the last 3 years' linear trend extrapolation:")
            console.print(f"Predicted trend price in 12 weeks: {format_value(predicted_price_12w)}", style=trend_color)
            console.print(Text(f"NOTE: This simple trend projection is highly unreliable for actual forecasting.", style="italic red"))


        # --- Logistic Regression for Next Day Direction Probability ---
        console.print("\n[bold]Logistic Regression (Probability of Up Move Tomorrow):[/bold]")
        log_df = hist_1y.copy() # Use 1 year data

        # Calculate features (example: RSI, MACD diff, % diff from SMA50)
        if len(log_df) > 14: log_df.ta.rsi(length=14, append=True)
        if len(log_df) > 30: log_df.ta.macd(fast=12, slow=26, signal=9, append=True)
        if len(log_df) > 50: log_df.ta.sma(length=50, append=True)

        # Ensure columns exist before calculating diffs
        if 'MACD_12_26_9' in log_df.columns and 'MACDs_12_26_9' in log_df.columns:
            log_df['MACD_diff'] = log_df['MACD_12_26_9'] - log_df['MACDs_12_26_9']
        else:
            log_df['MACD_diff'] = np.nan

        if 'SMA_50' in log_df.columns:
             log_df['SMA50_pct_diff'] = (log_df['Close'] - log_df['SMA_50']) / log_df['SMA_50'] * 100
        else:
             log_df['SMA50_pct_diff'] = np.nan

        # Target: 1 if next day's close is higher, 0 otherwise
        log_df['Target'] = (log_df['Close'].shift(-1) > log_df['Close']).astype(int)

        # Define features and drop NaNs
        features = ['RSI_14', 'MACD_diff', 'SMA50_pct_diff']
        log_df_clean = log_df.dropna(subset=features + ['Target']) # Drop rows where features or target are NaN


        if log_df_clean.empty or not all(f in log_df_clean.columns for f in features):
            console.print("Not enough data or indicators generated for Logistic Regression.", style="yellow")
        else:
            X_log = log_df_clean[features]
            y_log = log_df_clean['Target']

            if len(X_log) < 30 or len(y_log.unique()) < 2: # Need sufficient data and both classes (0 and 1)
                 console.print("Not enough data variance for Logistic Regression.", style="yellow")
            else:
                # Scale features
                scaler = StandardScaler()
                X_scaled = scaler.fit_transform(X_log)

                # Train model
                model_log = LogisticRegression(solver='liblinear', random_state=42)
                model_log.fit(X_scaled, y_log)

                # Predict probability for tomorrow based on *latest available* indicators in the clean df
                latest_features = log_df_clean[features].iloc[-1:] # Use last row from cleaned df
                # Convert prediction input to DataFrame with feature names to avoid warning
                latest_features_df = pd.DataFrame(latest_features.values, columns=features)
                latest_features_scaled = scaler.transform(latest_features_df) # Use the same scaler
                prob_tomorrow = model_log.predict_proba(latest_features_scaled)[0] # Prob for [class 0, class 1]

                prob_up = prob_tomorrow[1] # Probability of class 1 (price up)
                prob_color = "green" if prob_up > 0.5 else "red" if prob_up < 0.5 else "yellow"

                console.print(f"Based on latest technical indicators (RSI, MACD, SMA%):")
                console.print(f"Predicted probability of price increase tomorrow: {prob_up:.2%}", style=prob_color)
                console.print(Text(f"NOTE: This probability is model-based and not a guarantee.", style="italic red"))

    except Exception as e:
        console.print(f"\nAn error occurred: {e}", style="bold red")
        console.print("Please ensure the stock symbol is correct (e.g., 'RELIANCE.NS', 'INFY.NS') and you have an internet connection.", style="yellow")
        import traceback
        traceback.print_exc() # Print full traceback for debugging

# --- Script Execution ---
if __name__ == "__main__":
    # symbol_to_analyze = input("Enter Indian Stock Symbol (e.g., INFY.NS, RELIANCE.BO): ").strip().upper()
    symbol_to_analyze = "GAIL.NS"  #"IGL.NS" # Using IGL.NS as requested

    if not symbol_to_analyze:
        print("No symbol entered. Exiting.")
    else:
       analyze_stock(symbol_to_analyze)

    console.print("\n--- [bold]Disclaimer Reminder[/bold] ---", style="underline")
    console.print("Stock analysis involves risk. Data may be delayed. Predictions are speculative.", style="italic")
    console.print("This is NOT financial advice. Consult a professional before investing.", style="bold red")
