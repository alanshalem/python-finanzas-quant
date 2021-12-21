####################################################################################################
# Bot que encuentra las monedas que estan en minimos anuales de Binance y las imprime con la fecha y hora
####################################################################################################

import config as cfg  # Importo los datos de la API de Binance
from binance.client import Client  # Importo la libreria de Binance
from binance.enums import *  # Importo los enumerados de Binance
import datetime  # Importo la libreria de fechas

# Creo un cliente de Binance
client = Client(cfg.API_KEY, cfg.API_SECRET, tld='com')

# Obtengo todos los tickers de Binance
list_of_tickers = Client.get_all_tickers(client)
# Los datos vienen de la siguiente forma en los klines: [timestamp, precio_apertura, precio_maximo, precio_minimo, precio_cierre, cantidad_operaciones, volumen_operaciones]
for tick in list_of_tickers:
    klines = client.get_historical_klines(
        tick['symbol'], Client.KLINE_INTERVAL_8HOUR, "1 year ago UTC")
    if(len(klines) != 1098):
        continue
    print(len(klines))
    previous_close_price = klines[0][4]
    for i in range(1, len(klines)-1):
        if (previous_close_price > klines[i][4]):
            prev_close_price = klines[i][4]
            timestamp = datetime.datetime.fromtimestamp(
                int(str(klines[i][0])[:-3]))
    print('MINIMUM OF ' + tick['symbol'] + ' IS ' + str(prev_close_price) + ' IN DATE ' +
          timestamp.strftime('%Y-%m-%d') + ' AT ' + timestamp.strftime('%H:%M:%S'))
print(len(list_of_tickers))
