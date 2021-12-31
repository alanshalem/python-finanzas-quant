# Operadores Logicos
# Tablas de VERDAD
# Son solo esquemas de varios tipos de condiciones y operadores, por ejemplo,
# con el operador and el resultado  de unir dos condiciones A y B sera verdadero solo si ambas (AyB) son verdaderos
# Por otro lado, si uno dos condiciones A o B con el operador or, su resultado sera verdadero cuando ambas sean verdaderas,
# pero tambien cuando una de ellas es verdadera y la otra no

# TABLA DE VERDAD AND
# A	    B	    A y B
# False	False	False
# False	True	False
# True	False	False
# True	True	True

# TABLA DE VERDAD OR
# A	    B       A or B
# False	False	False
# False	True	True
# True	False	True
# True	True	True

# TABLA DE VERDAD NOT
# A	    not A
# False	True
# True	False

# TABLA de VERDAD XOR
# A	    B	    A ~ B
# False	False	False
# False	True	True
# True	False	True
# True	True	False

# Pero, todo esto es teorico, veamos esto con unos ejemplos.
# Supongamos el caso de tener un par de medias moviles,
# si una media movil rapida (por ejemplo de 20 periodos) es mayor (>)
# a una media movil lenta (por ejemplo de 100 periodos) entonces digamos
# que es un indicador de compra, y asociamos esa comparacion a una variable 'buySignal'
# Luego, supongamos que para comprar necesitamos preguntar si hay liquidez suficiente en la cuenta,
# por lo tanto, para gatillas una orden de compra vamos a tener que preguntar si el saldo de la cuenta
# es mayor a un determinado limite minimo y si es afirmativo definir como True la variable liquidez

smaFast = 20.4
smaLow = 20
price = 19
saldo = 15000

buySignal = smaFast > smaLow
liquidez = saldo > 1000

buy = buySignal and liquidez
print(buy)

# Ahora a nuestra logica le vamos a agregar el estado 'hold' que se va a mantener
# como True siempre que haya dado señal de compra y siempre y cuando el precio actual no sea
# menor a mi stopLoss
# Tambien se puede usar el operador not que lo que hace es preguntar por lo opuesto

smaFast = 20.4
smaSlow = 20
price = 19
saldo = 15000
stopLossPrice = 18  # precio de stopLoss

buySignal = smaFast > smaSlow
liquidez = saldo > 1000
stopLoss = (
    price <= stopLossPrice
)  # stopLoss, True si el precio es menor o igual al stopLossPrice, es decir, si de 19 baja a 18, cambia su valor a true

hold = buySignal and liquidez and not stopLoss
print(hold)
