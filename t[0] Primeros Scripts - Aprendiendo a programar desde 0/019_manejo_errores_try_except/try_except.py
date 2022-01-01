# La sentencia Try/Except es una forma de manejar errores en Python.
# Se usa para evitar que el script se corte inesperadamente por una cuenta
# o una instruccion que da error porque el interprete no puede resolverla.
# Recordemos que el flujo de informacion en un script es continuo y cualquier
# error que el interprete no sepa resolver va a cortar ese flujo y va a impedir que el script
# termine su rutina, por lo tanto, este metodo try/except nos va a permitir
# 'intentar' una instruccion que sospechamos puede dar error, y si ocurre el error realizar la
# instruccion que le pasamos en el 'except'
# Es como advertirle al interprete, "ojo que te mando esta instruccion dudosa, fijate primero si no es para quilombo"
# y ahi el interprete en lugar de seguir de una el flujo normal del script, lo que hace es ver si falla y si falla
# se va por el otro lado (el del except)
# Vamos a ver el ejemplo de la division por cero, hay veces que no sabemos si nos va a venir un dato vacio o no,
# y ahi es util usar este metodo.

# 1° Ejemplo
from typing import final


volumen = 1200
dias = 0

try:
    volMedio = volumen / dias
except:
    volMedio = None

print(volMedio)  # None -> ya que dias = 0, no se puede dividir por cero

# Otra manera
volumen = 1200
dias = 0
volMedio = None

try:
    volMedio = volumen / dias
except:
    pass  # La instruccion pass lo que hace es seguir de largo

print(volMedio)  # None -> ya que dias = 0, no se puede dividir por cero

# Por ultimo, tambien existe la instruccion finally que lo que hace es ejecutarse independientemente de si salio por el try o por el except
# Pasa siempre por el bloque finally, independientemente si haya habido un error o no.
volumen = 1200
dias = 2

try:
    volMedio = volumen / dias
except:
    volMedio = None
finally:
    print("Por aca pasa siempre")

print(volMedio)  # 1200/2 = 600

# ¿Para que sirve el bloque finally, si podria haber puesto esas lineas al mismo nivel que el except al terminar ese bloque?
# Es una cuestion mas bien de prolijidad, es exactamente lo mismo poner un bloque de instrucciones en el finally o ponerlo despues del bloque
# except sin mas, pero queda mas prolijo y entendible cuando todo el bloque Try/Except/Finally tiene una logica asociada.

# Mismo ejemplo con dias = 0
volumen = 1200
dias = 0

try:
    volMedio = volumen / dias
except:
    volMedio = None
finally:
    print("Por aca pasa siempre")
print(volMedio)  # None -> ya que dias = 0, no se puede dividir por cero
