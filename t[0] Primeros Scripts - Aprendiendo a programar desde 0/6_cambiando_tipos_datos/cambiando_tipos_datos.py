# NO ES UNA MUY BUENA IDEA CAMBIAR EL TIPO DE DATO YA QUE PUEDE CAMBIAR EL FLUJO DE UN PROGRAMA.
precio = 100.23433
print(precio, type(precio))  # > 100.23433 <class 'float'>

precio = int(precio)
print(precio, type(precio))  # > 100 <class 'int'> OJO! Nos trunca el dato


precio = str(precio)
print(precio, type(precio))  # > 100 < class 'str' >

# OJO! Andar jugando demasiado con los tipos de datos puede generar cosas inesperadas y de consecuencia impredecibles
print(precio*2)
