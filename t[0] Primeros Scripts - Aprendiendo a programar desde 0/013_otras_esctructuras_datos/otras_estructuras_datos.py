########################################################################################################################
# LISTAS
########################################################################################################################
# Listas: Las listas son un conjunto de datos y se lo define entre corchetes con sus elementos separados con coma.
# En otros lenguajes se los conocen como arreglos o arrays.
# Ejemplo:
#lista = [1,2,3,4,5]

# 1° forma de crear una lista
import random
lista_vacia = list()
print(lista_vacia)
#lista_vacia = []

# 2° forma de crear una lista
lista_vacia = []
print(lista_vacia)

# Lista con numeros de 1 a 4 con sintaxis de arreglos
lista_numeros = [1, 2, 3, 4]
print(lista_numeros)
# Lista con numeros de 1 a 4 con sintaxis list([])
lista_numeros_2 = list([1, 2, 3, 4])
print(lista_numeros_2)

# Lista con tipo de datos diferentes
listado = ['CERO', 1, 2, 'tres', 4.0, True]
print(listado)

print(type(listado))  # <class 'list'>

# Acceder a un elemento de la lista
print(listado[0])  # Accede al primer elemento de la lista (CERO)
print(listado[-1])  # Accede al ultimo elemento de la lista (True)
print(listado[-2])  # Accede al penultimo elemento de la lista (4.0)

############################################################################################################################
# Slicing de una lista: Se puede acceder a un rango de elementos de una lista, para recortar un "pedazo" de la lista accedo con el caracter ":". A la izquierda del ":" va el "DESDE" a la derecha de los ":" va el "HASTA"
# [DESDE:HASTA:PASO]
############################################################################################################################

print(listado[2:4])  # Accede al elemento 2 y 3 de la lista
print(listado[2:])  # Accede al elemento 2 y todos los siguientes de la lista
print(listado[:4])  # Accede al elemento 0, 1, 2 y 3 de la lista
print(listado[:])  # Accede todos los elementos de la lista
print(listado[:-2])  # Accede al elemento 0, 1, 2 y 3 de la lista
print(listado[-2:])  # Accede al 4 y 5 elemento de la lista
print(listado[:-4:-1])  # Accede al elemento 2, 3 y 4 de la lista

listado_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Accede a todos los elementos de la lista, pero saltando de 2 en 2
print(listado_2[::2])
print(listado_2[3::2])  # Accede al elemento 3, 5, 7, 9, 11 de la lista
# Accede a todos los elementos de la lista, pero al revés
print(listado_2[::-1])

# Longitud de una lista
print(len(listado))  # Devuelve el numero de elementos de la lista

# Index out of range
listado_3 = ["CERO", 1, 2, "tres", 4.0, True]
# print(listado_3[23]) # IndexError: list index out of range

# Cambiar valor de un elemento de la lista
listado_4 = ['GGAL', 'PAMP', 'YPFD', 'EDN', 'LOMA', 'CRES']
listado_4[1] = 'COME'
print(listado_4)

# Cambiar varios valores de la lista por un solo valor
listado_5 = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
listado_5[1:3] = ['COME']
print(listado_5)

# Cambiar varios elementos de la lista por varios valores
listado_5[1:3] = ['COME', 'COME']
print(listado_5)

# Eligiendo valores al azar de una lista
listado_6 = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
# Elegir un elemento al azar de la lista
print(random.choice(listado_6))
# Elegir n elementos al azar de la lista
print(random.sample(listado_6, 3))

# Reordenar aleatoriamente los elementos de una lista
random.shuffle(listado_6)
print(listado_6)

########################################################################################################################
# TUPLAS
########################################################################################################################
# Las tuplas son una estructura similar a las listas, pero son inmutables, es decir, una vez que las definimos, ya no les podemos cambiar valores.
# Son un conjunto de datos y se lo define entre parentesis con sus elementos separados con coma.
# Ejemplo:
#tupla = (1,2,3,4,5)

listado_tupla = ('GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES')
print(type(listado_tupla))  # <class 'tuple'>
print(listado_tupla[1])  # PAMP

# Vamos a provocar el error de querer asignar un nuevo valor a un elemento de una tupla.
# listado_tupla_1[1] = 'COME' # TypeError: 'tuple' object does not support item assignment

# ¿Que pasa si tengo una tupla y le quiero cambiar un valor? Uso los metodos para pasar de tupla a lista list() y viceversa tuple()
listado_tupla_2 = ('GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES')
print(type(listado_tupla_2))  # <class 'tuple'>
listado = list(listado_tupla_2)
print(type(listado))  # <class 'list'>
listado = tuple(listado)
print(type(listado))  # <class 'tuple'>

########################################################################################################################
# Metodos de tuplas y listas
########################################################################################################################

# Min y Max: Devuelve el valor mas pequeño y el mas grande de una tupla o lista
cantidades = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
print(min(cantidades))  # 2
print(max(cantidades))  # 10

# Index (donde aparece) y count (cuantas veces aparece) de un elemento en una tupla o lista
cantidades = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
print(cantidades.count(4))  # 2 (cuantas veces aparece el valor 4)
print(cantidades.index(6))  # 3 (donde aparece el valor 6)

# Sum: suma todos los elementos de una lista o tupla
cantidades = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
print(sum(cantidades))  # 60

# Sorted: Ordena los elementos de una lista o tupla
cantidades_tupla = (4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6)
cantidades_lista = [4, 2, 5, 6, 8, 10, 3, 5, 7, 4, 2, 6]
# [2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10] devuelve una lista ordenada a partir de la tupla
print(sorted(cantidades_tupla))
# [2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10] devuelve una lista ordenada a partir de una lista
print(sorted(cantidades_lista))

########################################################################################################################
# Metodos de listas
########################################################################################################################
# Sort: Ordena los elementos de una lista
cantidadesLista = list(cantidades)
cantidadesLista.sort()
print(cantidadesLista)  # [2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10]
cantidadesLista.sort(reverse=True)
print(cantidadesLista)  # [10, 8, 7, 6, 6, 5, 5, 4, 4, 3, 2, 2]

# Append: Agrega un elemento al final de la lista
listado = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
print(listado)  # ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
listado.append('ALUA')
# ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES', 'ALUA']
print(listado)

# Extend: Agrega varios elementos al final de la lista
listado = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
listadoPanelGral = ['BHIP', 'CELU', 'CTIO']
listado.extend(listadoPanelGral)
# ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES', 'BHIP', 'CELU', 'CTIO']
print(listado)

# Insert: Agrega un elemento en una posicion especifica de la lista
listado = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
listado.insert(3, 'TXAR')
# ['GGAL', 'PAMP', 'YPFD', 'TXAR', 'CEPU', 'EDN', 'LOMA', 'CRES']
print(listado)

# Pop: Elimina un elemento de la lista y devuelve el valor eliminado
listado = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
eliminado = listado.pop(2)  # YPFD
print('El elemento eliminado es: ' + eliminado)  # YPFD
print(listado)  # ['GGAL', 'PAMP', 'CEPU', 'EDN', 'LOMA', 'CRES']

# Reverse: Invierte los elementos de una lista
listado = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
listado.reverse()
print(listado)  # ['CRES', 'LOMA', 'EDN', 'CEPU', 'YPFD', 'PAMP', 'GGAL']

# Clear: Elimina todos los elementos de una lista
listado = ['GGAL', 'PAMP', 'YPFD', 'CEPU', 'EDN', 'LOMA', 'CRES']
listado.clear()
print(listado)  # []

########################################################################################################################
# Diccionarios
########################################################################################################################
# Un diccionario es una coleccion de datos que se almacenan en forma de clave-valor
# EjempLo:
diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23}
diccionario_acciones = {'ALUA': 29.35,
                        'BBAR': 120.85, 'BMA': 265.2, 'BYMA': 295}
type(diccionario)  # <class 'dict'>
type(diccionario_acciones)  # <class 'dict'>

print(diccionario['nombre'])  # Juan
print(diccionario['apellido'])  # Perez
print(diccionario_acciones['ALUA'])  # 29.35
# print(diccionario_acciones['BITCOIN']) # Si no existe la clave, devuelve un error
print(diccionario_acciones.get('ALUA'))  # 29.35
# Si no existe la clave, devuelve None (no existe)
print(diccionario_acciones.get('BITCOIN'))
# Si no existe la clave, devuelve el valor que se le pasa como segundo parametro
print(diccionario_acciones.get('BITCOIN', 'No existe la clave'))

# Acceder por separado a las Claves y los Valores
# dict_keys(['nombre', 'apellido', 'edad']) - Devuelve una lista con las claves
print(diccionario.keys())
# dict_values(['Juan', 'Perez', 23]) - Devuelve una lista con los valores
print(diccionario.values())

# Si queremos tener los valores como una lista, podemos hacerlo de la siguiente manera:
print(list(diccionario.values()))  # ['Juan', 'Perez', 23]

# Accedemos a los pares clave-valor
# dict_items([('nombre', 'Juan'), ('apellido', 'Perez'), ('edad', 23)]) - Devuelve una lista con los pares clave-valor
print(diccionario.items())

# Pop - Elimina un elemento del diccionario y devuelve el valor eliminado
print(diccionario.pop('edad'))  # 23
print(diccionario)  # {'nombre': 'Juan', 'apellido': 'Perez'}

# Update - Actualiza los valores de un diccionario
diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23}
diccionario.update({'nombre': 'Pedro', 'edad': 24})
print(diccionario)  # {'nombre': 'Pedro', 'apellido': 'Perez', 'edad': 24}
# otra forma
diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23}
diccionario.update(nombre='Pedro', edad=24)
print(diccionario)  # {'nombre': 'Pedro', 'apellido': 'Perez', 'edad': 24}
# otra forma
diccionario_1 = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23}
diccionario_2 = {'nombre': 'Pedro', 'edad': 24}
diccionario_1.update(diccionario_2)
print(diccionario_1)  # {'nombre': 'Pedro', 'apellido': 'Perez', 'edad': 24}

# Insertar nuevo elemento en un diccionario
dic1 = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23}
dic1['ciudad'] = 'Cordoba'
# {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23, 'ciudad': 'Cordoba'}
print(dic1)

# Inicializacion de Listas y Diccionarios
# Si quisieramos agregar elementos a listas o diccionarios que no existan, vamos a tener problemas.
# dicNuevo['ciudad'] = 'Cordoba'  # Error porque no existe la clave 'ciudad' en el diccionario dicNuevo
dicNuevo = {}
dicNuevo['GGAL'] = 29.35
print(dicNuevo)  # {'GGAL': 29.35}

listaNueva = []
listaNueva.append('GGAL')
print(listaNueva)  # ['GGAL']

#Asignacion multiple
lista1 = lista2 = lista3 = []
print(lista1, lista2, lista3)  # [] [] []
