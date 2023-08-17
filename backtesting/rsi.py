# import yfinance as yf
# import talib

# # Define the trading symbol and date range
# symbol = 'AAPL'
# start_date = '2023-01-01'
# end_date = '2023-08-10'

# # Fetch historical price data from Yahoo Finance using yfinance
# df = yf.download(symbol, start=start_date, end=end_date)

# # Calculate RSI
# rsi_period = 14
# df['rsi'] = talib.RSI(df['Close'], timeperiod=rsi_period)

# # Set RSI threshold values
# overbought_threshold = 70
# oversold_threshold = 30

# # Initialize trading position
# position = None

# # Iterate through the DataFrame and implement the RSI strategy
# for index, row in df.iterrows():
#     if row['rsi'] > overbought_threshold and position != 'short':
#         print(f"SELL Signal at {index}: RSI = {row['rsi']:.2f}")
#         position = 'short'
#     elif row['rsi'] < oversold_threshold and position != 'long':
#         print(f"BUY Signal at {index}: RSI = {row['rsi']:.2f}")
#         position = 'long'

# # Implement risk management, exit strategies, and other important aspects of the strategy.
import yfinance as yf
import numpy as np
import talib

# Define the symbol you want to trade
symbol = "BTCUSD"

# Fetch live data using yfinance
data = yf.download(symbol, period="1d", interval="1m")
print(data)

# Calculate RSI using talib
def calculate_rsi(data, period=14):
    close_prices = data["Close"].values
    rsi = talib.RSI(close_prices, timeperiod=period)
    return rsi

# Define RSI threshold for the strategy
rsi_threshold = 70

# Initialize positions and balances
position = 0
balance = 100000  # Starting balance

# Iterate through each data point
for i in range(len(data)):
    if i >= 14:  # Wait for enough data points for initial RSI calculation
        current_rsi = calculate_rsi(data[:i])
        
        if current_rsi[-1] > rsi_threshold and position == 0:
            # Buy signal: RSI above threshold and no position
            position = balance / data["Close"].iloc[i]
            balance = 0
            print(f"Buying at {data['Close'].iloc[i]}")
            
        elif current_rsi[-1] < (100 - rsi_threshold) and position > 0:
            # Sell signal: RSI below threshold and position held
            balance = position * data["Close"].iloc[i]
            position = 0
            print(f"Selling at {data['Close'].iloc[i]}")
            print(f"Profit: {balance - 100000}")
            
# Print final balance
if position > 0:
    balance = position * data["Close"].iloc[-1]
print(f"Final balance: {balance}")
