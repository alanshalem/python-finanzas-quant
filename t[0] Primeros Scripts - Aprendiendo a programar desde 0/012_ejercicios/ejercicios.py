#1- Hacer un script que devuelva en la variable año, el año actual.
#--------------------#
# Rta Ejercicio 1:
#--------------------#
import datetime as dt
from datetime import datetime as dt_dt
año = dt_dt.now().year
print(año)

#2- Escribir el codigo que asigne un dia y mes definidos en las primeras lineas en las variables dia y mes respectivamente, y que devuelva que dia de la semana cae esa fecha en el año actual.
#--------------------#
# Rta Ejercicio 2:
#--------------------#
import calendar as cal
dia = 1
mes = 1
año = dt_dt.now().year
print(cal.weekday(año, mes, dia))


#3- Hacer un script que le informe al usuario cuantos dias faltan para terminar el año
#--------------------#
# Rta Ejercicio 3:
#--------------------#
hoy = dt_dt.now()
año = dt_dt.now().year
mes = 12
dia = 31
fecha_fin_año = dt_dt(año, mes, dia)
dias_faltantes = fecha_fin_año - hoy
print(dias_faltantes.days)

#4- Hacer un script que le informe al usuario que fraccion de año queda para la expiracion de una opcion que vence el 18 de diciembre del corriente año (que funcione sea cual sea el año que se ejecute el codigo)
#--------------------#
# Rta Ejercicio 4:
#--------------------#
dia = 18
mes = 12
año = dt_dt.now().year
fecha_fin_año = dt_dt(año, mes, dia)
dias_faltantes = fecha_fin_año - hoy
print(dias_faltantes.days/365)