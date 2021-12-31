# La sentencia IF pregunta si se cumple o no una condición.
# En caso de que la condicion preguntada sea TRUE, se ejecuta la linea que sigue despues de los DOS PUNTOS
# En caso de que la condicion preguntada sea FALSE, si no hay else se termina, pero si hubiera un else, ejecuta la linea o lineas que siguen despues de los DOS PUNTOS del else

# Estructura del IF
# if(condicion):
#    linea1
#    linea2
# else:
#    linea1
#    linea2

# Ejemplo basico:
if True:
    print("La condicion es verdadera")
    print("Esto se ejecuta")
else:
    print("La condicion es falsa")
    print("Esto no se ejecuta")
print("Esto siempre se ejecuta")

# Evaluacion de True o False con distintos tipos de Variables
variableNula = None  # Python evalua las variables nulas como Falsas
if variableNula:
    print("La variable es verdadera")
else:
    print("La variable es falsa")

variableCero = 0  # Python evalua las variables cero como Falsas
if variableCero:
    print("La variable es verdadera")
else:
    print("La variable es falsa")

# Otro tipo de comparaciones
# 1
COME = 3
if COME < 4:
    print("La variable es verdadera")
else:
    print("La variable es falsa")

# 2
GGAL = 12
stopLoss = 11
if GGAL < stopLoss:
    print("Vender ya")
else:
    print("Sigo adentro")

# 3 - Es muy comun simplificar preguntando la condicion antes, por ejemplo:
GGAL = 12
stopLoss = GGAL < 11
if stopLoss:
    print("Vender ya")
else:
    print("Sigo adentro")
# La ventaja de esto es, por ejemplo, si tengo en vez de un stopLoss fijo, un trailing stopLoss, en ese caso, tendria que meter toda la logica dentro de la pregunta del IF
# Mientras mas compleja sea la logica, mas complicaria la lectura, es mas sencillo definir aparte la variable stopLoss a la cual incluso,
# como mas adelante veremos se le puede asignar la salida de una funcion y en el IF solo preguntar si se activo o no.
# Tambien tiene una ventaja en performance, en general, vamos a ver muchos ifs dentro de bucles o ciclos, si cada vez que evaluamos tenemos que preguntar si es verdadero o falso,
# estamos perdiendo milisegundos que pueden ser importantes en el agregado,
# asi que siempre es buena practica definir la evaluacion antes de una variable booleana y preguntar simplemente por esa variable.
# SIEMPRE busquemos la forma de definir las comparaciones antes y llegar al if con true o false.

# Otros operadores utiles
# Operador is not - "no es"
accion = "GGAL"
if accion is not GGAL:
    print("No es GGAL")
else:
    print("Es GGAL")

# Operador in - "esta en" (sirve para saber si un valor esta o no dentro de una lista)
accion = "YPF"
cartera = ["APPL", "AMZN", "FB"]
if accion in cartera:
    print(f"{accion} Esta en la cartera")
else:
    print(f"{accion} No esta en la cartera")
# YPF NO esta en la cartera

# Operador not - "no"
accion = "GGAL"
cartera = ["APPL", "AMZN", "FB"]
if accion not in cartera:
    print(f"Ojo que {accion} No esta en la cartera")
else:
    pass
# Ojo que GGAL No esta en la cartera

# La ventaja de usar este tipo de operadores es la claridad del codigo que se entiende por si solo.
