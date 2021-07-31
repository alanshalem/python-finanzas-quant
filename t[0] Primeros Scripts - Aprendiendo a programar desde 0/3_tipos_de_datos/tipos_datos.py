# NUMEROS ENTEROS int()
a = 5
print(type(a))  # int

# NUMEROS DECIMALES float()
a = 3.14
print(type(a))  # float

# BOOLEANOS (TRUE OR FALSE)
a = False  # OJO CON LA PRIMERA LETRA DE TRUE O FALSE, SI NO ES MAYUSCULA PYTHON NO LA RECONOCE
type(a)  # bool
a = True
print(type(a))  # bool

# STRINGS o CADENAS DE CARACTERES
a = "True"
print(type(a))  # string

# NULOS
a = None
print(type(a))

# OJO CON OPERAR VARIABLES DE DIFERENTE TIPO
a = 2  # int
b = a*3  # int
print(b)  # 6 = ✔️

a = "2"  # str
b = a*3  # str * 3
print(b)  # 222 = ❌

# ERRORES POR OPERAR TIPOS DE DATOS DIFERENTES

a = "2"
b = a + 3
print(b)  # TypeError: can only concatenate str (not "int") to str
# NO SE PUEDE CONCATENAR STRINGS CON ENTEROS

# PYTHON ES UN LENGUAJE INTERPRETADO, DINAMICAMENTE TIPADO, ES DECIR, UTILIZA UN INTERPRETE, LAS VARIABLES PUEDEN CAMBIAR SU TIPO DE DATO.
