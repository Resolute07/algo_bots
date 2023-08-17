import os
import sys
from pprint import pprint

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402


print('CCXT Version:', ccxt.__version__)

for exchange_id in ccxt.exchanges:
    try:
        exchange = getattr(ccxt, exchange_id)()
        print(exchange_id)
        
        # Load the market information for the exchange
        exchange.load_markets()
        
        # Print the available trading pairs
        pprint(list(exchange.markets.keys()))
    except Exception as e:
        print(e)