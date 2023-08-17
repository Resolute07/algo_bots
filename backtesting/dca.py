import ccxt
import time

# Initialize the exchange instance (replace 'binance' with your desired exchange)
exchange = ccxt.binance({
    'rateLimit': 2000,  # Number of requests per second
})

# Define the trading pair you're interested in (e.g., 'BTC/USDT' for Bitcoin against USDT)
symbol = 'BTC/USDT'

# Define the amount to invest in each DCA cycle
investment_amount = 100  # Amount in USDT

# Define the time interval for DCA (e.g., every 1 hour)
dca_interval = 3600  # Interval in seconds

while True:
    try:
        # Fetch live market data
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        
        print(f"Current Price: {current_price:.2f} USDT")
        
        # Perform DCA trade
        # Calculate the amount of the asset to buy based on the investment amount and current price
        asset_to_buy = investment_amount / current_price
        
        # Place the DCA order
        order = exchange.create_market_buy_order(symbol, asset_to_buy)
        print(f"DCA Order Placed: Bought {asset_to_buy:.6f} {symbol.split('/')[0]} at {current_price:.2f} USDT each")
        
        # Wait for the next DCA interval
        time.sleep(dca_interval)
        
    except Exception as e:
        print("An error occurred:", e)
        time.sleep(10)  # Retry after 10 seconds if an error occurs
