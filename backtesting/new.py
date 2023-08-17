from alpha_vantage.timeseries import TimeSeries
import talib
import time
import ccxt

# Replace with your Alpha Vantage API key
api_key = "D6TW3GD908H7Q0C6"

# Define the symbol for Bitcoin
symbol = "AAPL"  # This is the trading pair for Bitcoin against USD

# Initialize Alpha Vantage API client
ts = TimeSeries(key=api_key, output_format="pandas")

# Calculate RSI using talib
def calculate_rsi(data, period=14):
    close_prices = data["4. close"].values
    rsi = talib.RSI(close_prices, timeperiod=period)
    return rsi

# Define RSI threshold for the strategy
rsi_threshold = 70

# Initialize positions and balances
position = 0
balance = 100000  # Starting balance

while True:
    try:
        # Fetch live intraday data (adjust interval as needed)
        data, _ = ts.get_intraday(symbol=symbol, interval="1min", outputsize="compact")
        print(data)
        
        if len(data) >= 14:
            current_rsi = calculate_rsi(data)
            
            if current_rsi[-1] > rsi_threshold and position == 0:
                # Buy signal: RSI above threshold and no position
                position = balance / data["4. close"].iloc[-1]
                balance = 0
                print(f"Buying at {data['4. close'].iloc[-1]}")
                
            elif current_rsi[-1] < (100 - rsi_threshold) and position > 0:
                # Sell signal: RSI below threshold and position held
                balance = position * data["4. close"].iloc[-1]
                position = 0
                print(f"Selling at {data['4. close'].iloc[-1]}")
        
        # Print current balance
        print(f"Current balance: {balance}")
        
        # Print live price
        print(f"Live price: {data['4. close'].iloc[-1]}")
        
        # Wait for a while before the next iteration
        time.sleep(60)  # Sleep for 1 minute before checking again
        
    except Exception as e:
        print("An error occurred:", e)
        time.sleep(60)  # Retry after 1 minute if an error occurs
