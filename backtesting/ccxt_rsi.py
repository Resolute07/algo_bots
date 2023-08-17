import ccxt
import time
import talib
import numpy as np

# Initialize the exchange instance (replace 'binance' with your desired exchange)
exchange = ccxt.binance({
    'rateLimit': 2000,  # Number of requests per second
})

# Define the trading pair you're interested in (e.g., 'BTC/USDT' for Bitcoin against USDT)
symbol = 'BTC/USDT'

# Initialize the time interval for fetching data (e.g., '1m' for 1-minute interval)
timeframe = '1m'

# Initialize RSI period and threshold
rsi_period = 14
rsi_threshold = 70

while True:
    try:
        # Fetch live market data
        candles = exchange.fetch_ohlcv(symbol, timeframe)
        
        if len(candles) >= rsi_period:
            # Extract closing prices for RSI calculation
            close_prices = np.array([candle[4] for candle in candles], dtype=float)
            
            # Calculate RSI using talib
            rsi = talib.RSI(close_prices, timeperiod=rsi_period)
            current_rsi = rsi[-1]
            
            print(f"Current RSI: {current_rsi:.2f}")
            
            if current_rsi > rsi_threshold:
                print("RSI above threshold. Potential sell signal.")
            else:
                print("RSI below threshold. Potential buy signal.")
        
        # Wait for 10 seconds before fetching data again
        time.sleep(10)  # Sleep for 10 seconds before fetching the next candle
        
    except Exception as e:
        print("An error occurred:", e)
        time.sleep(10)  # Retry after 10 seconds if an error occurs
