import ccxt
# DEFINE YOUR EXCHANGE AND TICKERS:
my_exchange = 'Binance' # example of crypto exchange 
ticker1 = 'BTC' # first ticker of the crypto pair
ticker2 = 'USDT' # second ticker of the crypto pair
method_to_call = getattr(ccxt,my_exchange.lower()) # retrieving the # method from ccxt whose name matches the given exchange name
exchange_obj = method_to_call() # defining an exchange object
while True:
    pair_price_data = exchange_obj.fetch_ticker(ticker1+'/'+ticker2)
    closing_price = pair_price_data['close']
    print(closing_price)