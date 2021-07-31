# EJERCICIOS
# 1 - Obtener un precio aleatorio para la acción de GGAL que oscile entre 100 y 110 y con precisión de 0.01, asignarlo a la variable ggal
import random

min = 10000
max = 11000
paso = 1  # LA VARIABLE PASO DEBE SER INTEGER, POR LO TANTO DESPUES DIVIDO POR 100
ggal = random.randrange(min, max, paso)/100
print(ggal)

# 3 - Asumiendo que un activo tiene una distribución de sus rendimientos diarios muy similar a la distribución normal, y que su media diaria es de 0.1% con una volatilidad diaria del 2.5%.
# Escribir la instruccion que me devuelva valores aleatorios de su rendimiento diario.
media = 0.1
volatilidad = 2.5
print(random.normalvariate(media, volatilidad))
