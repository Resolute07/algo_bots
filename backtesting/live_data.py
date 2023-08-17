import ccxt
import time
import datetime
# Initialize the exchange instance (replace 'binance' with your desired exchange)
exchange = ccxt.binance({
    'rateLimit': 2000,  # Number of requests per second
})

# Define the trading pair you're interested in (e.g., 'BTC/USDT' for Bitcoin against USDT)
symbol = 'BTC/USDT'

# Initialize the time interval for fetching data (e.g., '1m' for 1-minute interval)
timeframe = '1m'

while True:
    try:
        # Fetch live market data
        candles = exchange.fetch_ohlcv(symbol, timeframe)

        # Print the latest candle (OHLCV: Open, High, Low, Close, Volume)
        latest_candle = candles[-1]
        timestamp, open_price, high_price, low_price, close_price, volume = latest_candle
        formatted_timestamp = datetime.datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Timestamp: {formatted_timestamp}, Close Price: {close_price}")

        # Wait for a while before fetching data again
        time.sleep(10)  # Sleep for 1 minute before fetching next candle
        
    except Exception as e:
        print("An error occurred:", e)
        time.sleep(10)  # Retry after 1 minute if an error occurs
