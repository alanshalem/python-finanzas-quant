# 1
string = "aapl"

# string.capitalize()
print(string.capitalize())  # 'Aapl'
# string.upper()
print(string.upper())  # 'AAPL'

# 2
string = "El dolar va a valer $211,11"

# string.title() # 'El Dolar Va A Valer $211,11'
print(string.title())

# 3
string = "El dolar esta caro, el dolar va a valer $211,11"

# string.rfind("str_buscado") => devuelve la ultima posicion donde aparece por primera vez el str_buscado en la variable string
print(string.rfind("dolar"))  # ['E', 'l', ' ', 'd', 'o', 'l', 'a', 'r']
# string.find() => devuelve la ultima posicion donde aparece por primera vez el str_buscado en la variable string
print(string.find("dolar"))
# string.replace("str_buscado", "str_reemplazo") => reemplaza "str_buscado" por "str_reemplazo" en la variable string
# 'El euro esta caro, el euro va a valer $211,11'
print(string.replace("dolar", "euro"))

# 4
string = "1"

# string.zfill(largo) => rellena con ceros a la izquierda hasta completar el largo pasado como argumento
print(string.zfill(3))  # '001

# 5
string = "Dolares, dolares y mas dolares"

# string.count("string buscado") => devuelve la cantidad de veces que aparece el string buscado en la variable string
# '2' OJO! Es case sensitive, no es lo mismo 'Dolares' que 'dolares'
print(string.count("dolares"))

# len(string) => cuenta la cantidad de caracteres de la variable string
print(len(string))

# string.isalnum() => devuelve true si todos los caracteres son alfanumericos
# string.isalpha() => devuelve true si todos los caracteres son letras
# string.isnum() => devuelve true si todos los caracteres son numeros
string = "123"
print(string.isalpha())  # FALSE
print(string.isdigit())  # TRUE
print(string.isalnum())  # TRUE
