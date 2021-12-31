# Decisiones Consecutivadas o Concatenadas
# Son muy utiles cuando tenemos que ir preguntando algo que en lugar de ser blanco/negro o si/no se va dividiendo como en grupos o escalas,
# por ejemplo, para rangos de malo, regular, bueno, muy bueno, excelente, vamos a evaluar una variable consecutivamente con los limites de esos grupos,
# veamos primero la estructura de las decisiones consecutivas.

# if condicion_1:
#     acciones si condicion_1 es verdadera
# elif condicion_2:
#     acciones si condicion_2 es verdadera
# ......
# elif condicion_n:
#   acciones si condicion_n es verdadera
# else:
#   acciones si no fue verdadera ninguna de las condiciones anteriores
# sigue el programa

# Ejemplo tipico de decisiones consecutivas
merval = 1800
if merval > 1500:
    print("All in Argy")
elif merval > 1000:
    print("Es por aca")
else:
    print("Piña historica")

# Decisiones Anidadas
# Las decisiones anidadas son ni mas ni menos que una decision adentro de otra.
# Veamos un ejemplo:
merval = 1200
usd = 60
if merval > 800:
    if usd < 40:
        print("All in Argy")
    else:
        print("All in Brasil")
else:
    if usd < 40:
        print("Piña historica")
    else:
        print("Yo te avise")
