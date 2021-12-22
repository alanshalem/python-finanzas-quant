####################################################################################################
# Bot que encuentra las monedas que estan en minimos anuales de Binance y las imprime con la fecha y hora
####################################################################################################

import datetime  # Importo la libreria de fechas

from binance.client import Client  # Importo la libreria de Binance
from binance.enums import *  # Importo los enumerados de Binance

import config as cfg  # Importo los datos de la API de Binance

# Creo un cliente de Binance
client = Client(cfg.API_KEY, cfg.API_SECRET, tld="com")
MINIMUMS = {}  # Creo un diccionario para almacenar los minimos anuales

# Obtengo todos los tickers de Binance
list_of_tickers = Client.get_all_tickers(client)
# Los datos vienen de la siguiente forma en los klines: [timestamp, precio_apertura, precio_maximo, precio_minimo, precio_cierre, cantidad_operaciones, volumen_operaciones]
for tick in list_of_tickers:
    if (
        tick["symbol"][-3:] != "BNB"
    ):  # Si el ticker termina en BNB, solo considero ese par
        continue
    klines = client.get_historical_klines(
        tick["symbol"], Client.KLINE_INTERVAL_8HOUR, "1 year ago UTC"
    )
    # print(len(klines))
    if len(klines) != 1095:
        continue
    previous_close_price = klines[0][4]
    for i in range(1, len(klines) - 1):
        if previous_close_price > klines[i][4]:
            prev_close_price = klines[i][4]
            timestamp = datetime.datetime.fromtimestamp(int(str(klines[i][0])[:-3]))
    print(
        "MINIMUM OF "
        + tick["symbol"]
        + " IS "
        + str(prev_close_price)
        + " IN DATE "
        + timestamp.strftime("%Y-%m-%d")
        + " AT "
        + timestamp.strftime("%H:%M:%S")
    )
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == tick["symbol"]:
            current_price_of_symbol = float(tick_2["price"])
    if (
        current_price_of_symbol
        < float(prev_close_price) + float(prev_close_price) * 0.05
    ):
        print(
            "ESTE ESTA EN MINIMO ANUAL -----> " + tick["symbol"] + " " + tick["price"]
        )
        MINIMUMS[tick["symbol"]] = tick["price"]


# print(len(list_of_tickers))
print("************************************************************")
print(MINIMUMS)
print(len(MINIMUMS))
