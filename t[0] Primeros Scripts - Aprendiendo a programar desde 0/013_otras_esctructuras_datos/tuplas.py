########################################################################################################################
#TUPLAS
########################################################################################################################
# Las tuplas son una estructura similar a las listas, pero son inmutables, es decir, una vez que las definimos, ya no les podemos cambiar valores.
# Son un conjunto de datos y se lo define entre parentesis con sus elementos separados con coma.
#Ejemplo:
#tupla = (1,2,3,4,5)

listado_tupla = ('GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES')
print(type(listado_tupla)) # <class 'tuple'>
print(listado_tupla[1]) # PAMP

#Vamos a provocar el error de querer asignar un nuevo valor a un elemento de una tupla.
#listado_tupla_1[1] = 'COME' # TypeError: 'tuple' object does not support item assignment

# ¿Que pasa si tengo una tupla y le quiero cambiar un valor? Uso los metodos para pasar de tupla a lista list() y viceversa tuple()
listado_tupla_2 = ('GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES')
print(type(listado_tupla_2)) # <class 'tuple'>
listado = list(listado_tupla_2)
print(type(listado)) # <class 'list'>
listado = tuple(listado)
print(type(listado)) # <class 'tuple'>

########################################################################################################################
#Metodos de tuplas y listas
########################################################################################################################

#Min y Max: Devuelve el valor mas pequeño y el mas grande de una tupla o lista
cantidades = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
print(min(cantidades)) # 2
print(max(cantidades)) # 10

#Index (donde aparece) y count (cuantas veces aparece) de un elemento en una tupla o lista
cantidades = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
print(cantidades.count(4)) # 2 (cuantas veces aparece el valor 4)
print(cantidades.index(6)) # 3 (donde aparece el valor 6)

# Sum: suma todos los elementos de una lista o tupla
cantidades = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
print(sum(cantidades)) # 60

# Sorted: Ordena los elementos de una lista o tupla
cantidades_tupla = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
cantidades_lista = [4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6]
print(sorted(cantidades_tupla)) # [2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10] devuelve una lista ordenada a partir de la tupla
print(sorted(cantidades_lista)) # [2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10] devuelve una lista ordenada a partir de una lista
