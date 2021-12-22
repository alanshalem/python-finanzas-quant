# EJERCICIO 1
# Dada la siguiente lista:
# listado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# 1 - Los numeros pares
# 2 - Los valores del 4 hasta el final de la lista
# 3 - Los valores del 5 hasta el 10
# 4 - Los valores menores a 10 que sean pares
# 5 - Los multiplos de 3 ordenados al reves
# 6 - El promedio de todos los numeros (usando las funciones sum y len)

import random

listado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# 1 - Los numeros pares
print(listado[1::2])
# 2 - Los valores del 4 hasta el final de la lista
print(listado[3:])
# 3 - Los valores del 5 hasta el 10
print(listado[4:10])
# 4 - Los valores menores a 10 que sean pares
print(listado[1:-3:2])
# 5 - Los multiplos de 3 ordenados al reves
print(listado[-1::-3])
# 6 - El promedio de todos los numeros (usando las funciones sum y len)
print(sum(listado) / len(listado))

# Dadas las siguientes listas:
# lideres = ['GGAL', 'PAMP', 'YPFD', 'TECO2', 'EDN', 'LOMA', 'BBAR']
# galpones = ['AGRO', 'FIPL', 'MIRG', 'GARO', 'LONG']
# 7 - Elegir un galpon al azar y agregarlo a la lista de lideres al final
lideres = ["GGAL", "PAMP", "YPFD", "TECO2", "EDN", "LOMA", "BBAR"]
galpones = ["AGRO", "FIPL", "MIRG", "GARO", "LONG"]

lideres.append(galpones.pop(random.randint(0, len(galpones) - 1)))
print(lideres)

# 8 - Elegir un galpon al azar y reemplazar a EDN por ese galpon
galpones.pop(random.randint(0, len(galpones) - 1))  # Selecciono un galpon al azar
lideres[lideres.index("EDN")] = galpones.pop(
    random.randint(0, len(galpones) - 1)
)  # Reemplazo a EDN por el galpon seleccionado

# 9 - Elegir 3 galpones al azar y reemplazar una lider cualquiera por esos dos galpones
# Elegir 3 galpones al azar
galpones_elegidos = random.sample(galpones, 3)
indice = random.randint(0, len(lideres) - 1)
lideres[indice] = galpones_elegidos.pop(random.randint(0, len(galpones_elegidos) - 1))

# EJERCICIO 2
# Dado el siguiente diccionario:
# panel = {'ALUA': 29.3, 'BBAR': 120.5, 'BMA': 265.2, 'BYMA': 290, 'CEPU': 29, 'COME': 3, 'CRES': 40.7}
# 10 - Reemplazar el precio de BBAR por un precio al azar que elija python que varie +/- $1 del precio que tiene (con precision de 0.01)
# 11 - Reemplazar el precio de BBAR por un precio al azar que elija python que varie +/- 3% del precio que tiene (con precision de 0.01)
# 12 - Elegir un ticker al azar y mostrarlo
# 13 - Re-ordenar el diccionario al azar
# 14 - Re-ordenar el diccionario alfabeticamente en forma inversa (de la Z a la A)

panel = {
    "ALUA": 29.3,
    "BBAR": 120.5,
    "BMA": 265.2,
    "BYMA": 290,
    "CEPU": 29,
    "COME": 3,
    "CRES": 40.7,
}

# 10 - Reemplazar el precio de BBAR por un precio al azar que elija python que varie +/- $1 del precio que tiene (con precision de 0.01)
panel["BBAR"] = round(panel["BBAR"] + random.uniform(-1, 1), 2)

# 11 - Reemplazar el precio de BBAR por un precio al azar que elija python que varie +/- 3% del precio que tiene (con precision de 0.01)

# 12 - Elegir un ticker al azar y mostrarlo

# 13 - Re-ordenar el diccionario al azar

# 14 - Re-ordenar el diccionario alfabeticamente en forma inversa (de la Z a la A)
