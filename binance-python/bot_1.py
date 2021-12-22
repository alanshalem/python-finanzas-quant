####################################################################################################
# Bot que imprime el precio de los pares y la cantidad de pares listados en Binance
####################################################################################################

from binance.client import Client  # Importo la libreria de Binance
from binance.enums import *  # Importo los enumerados de Binance

import config as cfg  # Importo los datos de la API de Binance

# Creo un cliente de Binance
client = Client(cfg.API_KEY, cfg.API_SECRET, tld="com")

# Obtengo todos los tickers de Binance
list_of_tickers = Client.get_all_tickers(client)
#  Imprime todos los pares disponibles en Binance
print(list_of_tickers)
# Imprime el numero de pares disponibles en Binance
print(len(list_of_tickers))
