# Ejercicios
# Partiendo de las siguientes variables:
# - price que tiene el precio actual del activo en el mercado
# - buyPrice que tiene el valor al que compramos el activo al ingresarlo en la cartera
# - smaFast y smaSlow que son dos medias moviles que usaremos para saber si esta en tendencia
# Ir modificando la variable price para verificar que el script anda. Configurar las variables con los siguientes valores:
# smaFast = 100
# smaSlow = 98
# buyPrice = 106

# 1- Armar un script que me defina en una sola condicion la variable hold para un activo es verdadera o falsa, en funcion de las siguientes premisas:
# Que este en tendencia bull, asumiendo para ello que la media rapida sea un 2% mayor a una media lenta
# Que no rompa un stopLoss del 5% abajo del precio de compra
# Que la ganancia acumulada no sea superior al 20% ya que en ese caso se tomaria ganancias
# Y verificar que nos devuelve para los siguientes precios:
# -price=97 => False
# -price=100 => False
# -price=101 => True
# -price=121 => True
# -price=128 => False

# 2- Con las mismas premisas del ejercicio anterior, modificarlo para que me devuelva en una
# variable state un string que me indique si sigo invertido en ese activo, pero ademas en caso de ser
# falso me indique si se salio por stopLoss o por toma de ganancias
# Verificar que nos devuelve lo siguiente para los siguientes precios:
# -price=97 => Salida por stopLoss
# -price=100 => Salida por stopLoss
# -price=101 => Invertidos
# -price=121 => Invertidos
# -price=128 => Salida por takeProfit

# 3- Reforzar la logica del ejercicio anterior agregando a la condicion del stopLoss que el
# precio tiene que cortar a la media movil lento para abajo para disparar el stopLoss. Verificar que
# nos devuelve lo siguiente para los siguientes precios.
