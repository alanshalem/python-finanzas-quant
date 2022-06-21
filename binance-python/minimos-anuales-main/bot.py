import config
from binance.client import Client
from binance.enums import *
import datetime

client = Client( config.API_KEY, config.API_SECRET, tld='com' )
MINIMUMS = []

list_of_tickers = client.get_all_tickers()
for tick in list_of_tickers:
    if (tick['symbol'][-3:] != 'BNB'):
        continue
        
    klines = client.get_historical_klines(tick['symbol'], Client.KLINE_INTERVAL_8HOUR, "1 year ago UTC")
    if (len(klines) != 1098):
        continue
    prevClose_Price = klines[0][4]
    for i in range (1, len(klines)-1):
        if (prevClose_Price > klines[i][4]):
            prevClose_Price = klines[i][4]
            timestamp = datetime.datetime.fromtimestamp(int(str(klines[i][0])[:-3]))

    print("MINIMUM OF " + tick['symbol'] + " IS "+ str(prevClose_Price) + " IN DATE " + timestamp.strftime('%Y-%m-%d %H:%M:%S'))

    for tick_2 in list_of_tickers:
        if tick_2['symbol'] == tick['symbol']:
            currentPrice_of_Symbol = float(tick_2['price'])
    if currentPrice_of_Symbol < float(prevClose_Price) + float(prevClose_Price) * 0.05:
        print("ESTE ESTÁ EN MINIMO ANUAL --------> "+ tick['symbol'])
        MINIMUMS.append(tick['symbol'])

print("**************************")
print(MINIMUMS)
print(len(MINIMUMS))
