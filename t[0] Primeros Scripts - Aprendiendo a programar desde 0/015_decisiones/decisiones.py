# OPERADORES RELACIONALES
# IGUALDAD: ==
# DISTINTO: !=
# MAYOR QUE: >
# MAYOR O IGUAL QUE: >=
# MENOR QUE: <
# MENOR O IGUAL QUE: <=

COME = 3
GGAL = 100

print(COME > GGAL)  # 3>100 - False
print(COME <= GGAL)  # 3<=100 - True
print(COME == GGAL)  # 3==100 - False
print(COME != GGAL)  # 3!=100 - True
# Comparar un numero con un string
# print(COME > "COME")  # TypeError: '>' not supported between instances of 'int' and 'str'
# En este caso comparar un numero con un string no da error porque estamos preguntando si son distintos
print(COME != "COME")  # 3!="COME" - False
# TRUE = 1 y FALSE = 0
print(COME > True)  # 3>1 - True
print(COME == True)  # 3==1 - False
print(1 == True)  # 1==1 - True
print(1 <= True)  # 1<=1 - True
print(0 == False)  # 0==0 - True
print(COME == None)  # 3==None - False
# print(COME > None)  # 3>None - TypeError: '>' not supported between instances of 'int' and 'NoneType'
# Si bien el valor de None es 0 (el mismo que false) si evaluo comparar una variable nula con el 0 me devuelve falso,
# porque python no tiene comparacion de igualdad estricta, por lo tanto, la igualdad es estricta de por si
