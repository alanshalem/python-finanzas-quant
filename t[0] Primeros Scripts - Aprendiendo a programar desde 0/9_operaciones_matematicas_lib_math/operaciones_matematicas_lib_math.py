import math

# CONSTANTES
# NUMERO PI
print(math.pi)
# NUMERO E
e = math.e
print(e)

# REDONDEO Y TRUNCADO
# ENTERO INMEDIATO INFERIOR
print(math.floor(5.44))  # 5
# ENTERO INMEDIATO SUPERIOR
print(math.ceil(5.44))  # 6
# ENTERO
print(math.trunc(-5.34))  # -5
# REDONDEAR POR CANTIDAD DE DECIMALES
print(round(5.76543, 3))  # 5.765

# LOGARITMOS
print(math.log(100, 10))  # 2.0

e = math.exp(1)
print(math.log(e))  # 1.0

# OTRAS FUNCIONES
# MULTIPLO COMUN DIVISOR, FACTORIAL, ETC...
print(math.gcd(9, 24))  # 3
print(math.factorial(6))  # 6.5.4.3.2.1 = 720

# IS CLOSE - sirve para decidir si un numero esta cerca de otro o no en funcion de una tolerancia porcentual
a = 989
b = 1000
tol = 0.05
print(math.isclose(a, b, rel_tol=0.1))  # TRUE
print(math.isclose(a, b, rel_tol=0.01))  # FALSE
