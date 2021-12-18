########################################################################################################################
#LISTAS
########################################################################################################################
#Listas: Las listas son un conjunto de datos y se lo define entre corchetes con sus elementos separados con coma. 
# En otros lenguajes se los conocen como arreglos o arrays.
#Ejemplo:
#lista = [1,2,3,4,5]

# 1° forma de crear una lista
lista_vacia = list()
print(lista_vacia)
#lista_vacia = []

# 2° forma de crear una lista
lista_vacia = []
print(lista_vacia)

#Lista con numeros de 1 a 4 con sintaxis de arreglos
lista_numeros = [1,2,3,4]
print(lista_numeros)
# Lista con numeros de 1 a 4 con sintaxis list([])
lista_numeros_2 = list([1,2,3,4])
print(lista_numeros_2)

# Lista con tipo de datos diferentes
listado = ['CERO', 1, 2, 'tres', 4.0, True] 
print(listado)

print(type(listado)) # <class 'list'>

# Acceder a un elemento de la lista
print(listado[0]) # Accede al primer elemento de la lista (CERO)
print(listado[-1]) # Accede al ultimo elemento de la lista (True)
print(listado[-2]) # Accede al penultimo elemento de la lista (4.0)

############################################################################################################################
#Slicing de una lista: Se puede acceder a un rango de elementos de una lista, para recortar un "pedazo" de la lista accedo con el caracter ":". A la izquierda del ":" va el "DESDE" a la derecha de los ":" va el "HASTA"
#[DESDE:HASTA:PASO]
############################################################################################################################

print(listado[2:4]) # Accede al elemento 2 y 3 de la lista
print(listado[2:]) # Accede al elemento 2 y todos los siguientes de la lista
print(listado[:4]) # Accede al elemento 0, 1, 2 y 3 de la lista
print(listado[:]) # Accede todos los elementos de la lista
print(listado[:-2]) # Accede al elemento 0, 1, 2 y 3 de la lista
print(listado[-2:]) # Accede al 4 y 5 elemento de la lista
print(listado[:-4:-1]) # Accede al elemento 2, 3 y 4 de la lista

listado_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(listado_2[::2]) # Accede a todos los elementos de la lista, pero saltando de 2 en 2
print(listado_2[3::2]) # Accede al elemento 3, 5, 7, 9, 11 de la lista
print(listado_2[::-1]) # Accede a todos los elementos de la lista, pero al revés

#Longitud de una lista
print(len(listado)) # Devuelve el numero de elementos de la lista

# Index out of range
