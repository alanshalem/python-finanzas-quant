
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
