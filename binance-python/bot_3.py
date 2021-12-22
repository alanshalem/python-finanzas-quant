####################################################################################################
# Bot que tiene stop loss dinamicos
####################################################################################################
# Ejemplo simple del funcionamiento del algoritmo:
# Si tenemos una moneda a 45.00 y queremos comprar, ejecutamos el proceso y se pone una orden de compra a 48.00
# Si el precio baja a 40.00, se cancela la orden de compra y se pone una nueva orden de venta a 43.00
# Si el precio vuelve a baja a 35.00, se cancela la orden de venta y se pone una nueva orden de compra a 38.00
# Si el precio sube, se ejecuta la orden de compra en 38.00

import time  # Importo la libreria de fechas

# import numpy as np  # Importo la libreria de numpy
from binance.client import Client  # Importo la libreria de Binance
from binance.enums import *  # Importo los enumerados de Binance

import config as cfg  # Importo los datos de la API de Binance

# Creo un cliente de Binance
client = Client(cfg.API_KEY, cfg.API_SECRET, tld="com")
symbol_ticker = "BNBUSDT"  # Par de moneda
quantity = 1  # Cantidad de monedas a operar
prev_symbol_price = 0.0
SIDE_BUY = "BUY"  # Tipo de operacion
ORDER_TYPE_LIMIT = "STOP_LOSS_LIMIT"  # Tipo de orden
TIME_IN_FORCE_GTC = "GTC"  # Tiempo de vida de la orden


list_of_tickers = Client.get_all_tickers(client)  # Obtengo todos los tickers de Binance
for tick_2 in list_of_tickers:
    if tick_2["symbol"] == symbol_ticker:
        prev_symbol_price = float(tick_2["price"])


buyOrder = client.create_order(
    symbol=symbol_ticker,
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    quantity=quantity,
    price=round(
        prev_symbol_price * 1.01, 1
    ),  # Precio de compra, redondeamos a 7 decimales porque BNBBTC tiene una precisión de 4 decimales, si pongo 5, da error
    stopPrice=round(
        prev_symbol_price * 1.02, 1
    ),  # Precio de compra, redondeamos a 7 decimales porque BNBBTC tiene una precisión de 4 decimales, si pongo 5, da error
    timeInForce=TIME_IN_FORCE_GTC,
)

while 1:
    time.sleep(5)
    list_of_tickers = Client.get_all_tickers(
        client
    )  # Obtengo todos los tickers de Binance
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == symbol_ticker:
            current_symbol_price = float(tick_2["price"])

    print("PREVIOUS PRICE: " + str(prev_symbol_price))
    print("CURRENT PRICE: " + str(current_symbol_price))

    if prev_symbol_price > current_symbol_price:
        result = client.cancel_order(
            symbol=symbol_ticker,
            orderId=buyOrder.get("orderId"),
        )

        buyOrder = client.create_order(
            symbol=symbol_ticker,
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=round(
                current_symbol_price + 0.01, 1
            ),  # Precio de compra, redondeamos a 7 decimales porque BNBBTC tiene una precisión de 4 decimales, si pongo 5, da error
            stop_price=round(
                current_symbol_price + 0.02, 1
            ),  # Precio de compra, redondeamos a 7 decimales porque BNBBTC tiene una precisión de 4 decimales, si pongo 5, da error
            timeInForce=TIME_IN_FORCE_GTC,
        )

        prev_symbol_price = current_symbol_price
