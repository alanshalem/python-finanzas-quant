########################################################################################################################
# LIBRERIA DATETIME
########################################################################################################################

import datetime as dt
# LA LIBRERIA DATETIME TIENE LOS SIGUIENTES PAQUETES O SUBLIBRERIA: date - time - datetime - timedelta - timezone - tzinfo
# IMPORTANDO SUB-PAQUETES
from datetime import datetime as dt_dt
from datetime import date as dt_date
# ESOS ALIAS (dt_dt - dt_date) NOS PERMITEN REFERIRNOS EN MODO MAS ABREVIADO A LOS SUBPAQUETES.
# EN LUGAR DE datetime.datetime SOLO DIREMOS dt_dt
# EN LUGAR DE datetime.date SOLO DIREMOS dt_date


hoy = dt_dt.now()
print(hoy, type(hoy))  # FECHA CON HORA

hoy = dt_date.today()
print(hoy, type(hoy))  # FECHA SIN HORA

hoy = dt_dt.today().ctime()
print(hoy, type(hoy))  # FECHA CON HORA Y FORMATO DE TEXTO

print('########################################################################################################################')

#CONVERTIR UN STRING EN UN OBJETO DATETIME
hoy = dt_dt.today() # CREO LA VARIABLE hoy CON LA FECHA ACTUAL EN FORMATO DATETIME
expiracion_str = '2022-12-16' # CREO LA VARIABLE expiracion_str CON LA FECHA DE EXPIRACION EN FORMATO STRING
expiracion = dt_dt.strptime(expiracion_str, '%Y-%m-%d') # CONVIERTO LA FECHA DE EXPIRACION EN FORMATO STRING A FORMATO DATETIME
print("Expiracion: ", expiracion, " - Tipo de dato de expiracion", type(expiracion)) # IMPRIMO LA FECHA DE EXPIRACION

vencimiento = expiracion - hoy # CALCULO LA DIFERENCIA ENTRE LA FECHA DE EXPIRACION Y LA FECHA ACTUAL
print("Vencimiento: ", vencimiento, " - Tipo de dato de vencimiento", type(vencimiento))  # RESULTADO: DIFERENCIA DE DIAS ENTRE LA FECHA DE EXPIRACION Y LA FECHA ACTUAL

dias_vencimiento = vencimiento.days # EXTRAIGO LOS DIAS DE LA DIFERENCIA ENTRE LA FECHA DE EXPIRACION Y LA FECHA ACTUAL
segundos = vencimiento.seconds # EXTRAIGO LOS SEGUNDOS DE LA DIFERENCIA ENTRE LA FECHA DE EXPIRACION Y LA FECHA ACTUAL
print("Dias restantes: ", dias_vencimiento, "\nSegundos restantes:", segundos)  # RESULTADO: DIAS Y SEGUNDOS PARA EL VENCIMIENTO


print(dt_dt.ctime(expiracion))  # ACCEDO AL STRING DE LA FECHA DE EXPIRACION QUE YA ESTA EN FORMATO DATETIME
print('########################################################################################################################')

########################################################################################################################
#GENERAR UNA FECHA COMO OBJETO DATETIME
########################################################################################################################

año = 2020
mes = 12
dia = 16
hora = 12
minutos = 30
segundos = 0

fecha = dt_dt(año, mes, dia, hora, minutos, segundos) # CREO LA VARIABLE fecha DE TIPO DATETIME CON VALORES QUE DESEO
print(fecha, type(fecha)) # IMPRIMO LA FECHA CON HORA

#AHORA, SI QUIERO CONVERTIR LA FECHA QUE YA TENGO EN FORMATO DATETIME A FORMATO STRING USO LA FUNCION str()
fecha_str = str(fecha) # CONVIERTO LA FECHA EN FORMATO DATETIME A FORMATO STRING
print('########################################################################################################################')

########################################################################################################################
#DISTINTOS FORMATOS PARA MOSTRAR FECHAS
########################################################################################################################

hoy = dt_dt.today() # CREO LA VARIABLE hoy CON LA FECHA ACTUAL EN FORMATO DATETIME
hoy_txt = dt_dt.strftime(hoy, '%d/%m/%Y') # CONVIERTO LA FECHA ACTUAL EN FORMATO DATETIME A FORMATO STRING
print(hoy) # IMPRIMO LA FECHA ACTUAL EN FORMATO DATETIME
print(hoy_txt) # IMPRIMO LA FECHA ACTUAL EN FORMATO STRING
print('########################################################################################################################')

########################################################################################################################
#SETEO DE PARAMETRIZACION LOCAL
#Fechas y horas: locale.LC_TIME
# Signos y nomenclaturas monetarias: locale.LC_MONETARY
# Numeracion y signos de puntuacion: locale.LC_NUMERIC
# Nombres y nomenclaturas de paises: locale.LC_NAME
########################################################################################################################


import locale # IMPORTO LA LIBRERIA LOCALE
from datetime import datetime as dt_dt # IMPORTO LA LIBRERIA DATETIME Y LE ASIGNO EL ALIAS dt

locale.setlocale(locale.LC_TIME, 'en') # SETEO LA LOCALIZACION DE LA FECHA EN FORMATO LOCAL EN INGLES
hoy = dt_dt.today() # CREO LA VARIABLE hoy CON LA FECHA ACTUAL EN FORMATO DATETIME CON LA LOCALIZACION SETEADA EN INGLES
print(hoy) # IMPRIMO LA FECHA ACTUAL EN FORMATO DATETIME CON LA LOCALIZACION SETEADA EN INGLES
hoy = dt_dt.strftime(hoy, '%A %d %B %Y') # CONVIERTO LA FECHA ACTUAL EN FORMATO DATETIME A FORMATO LOCAL
print(hoy) # IMPRIMO LA FECHA ACTUAL EN FORMATO LOCAL CON LA LOCALIZACION SETEADA EN INGLES

locale.setlocale(locale.LC_TIME, 'es') # SETEO LA LOCALIZACION DE LA FECHA EN FORMATO LOCAL EN ESPAÑOL
hoy_es = dt_dt.today() # CREO LA VARIABLE hoy CON LA FECHA ACTUAL EN FORMATO DATETIME CON LA LOCALIZACION SETEADA EN ESPAÑOL
print(hoy_es) # IMPRIMO LA FECHA ACTUAL EN FORMATO DATETIME CON LA LOCALIZACION SETEADA EN ESPAÑOL
hoy_es = dt_dt.strftime(hoy_es, '%A %d de %B %Y') # CONVIERTO LA FECHA ACTUAL EN FORMATO DATETIME A FORMATO LOCAL
print(hoy_es) # IMPRIMO LA FECHA ACTUAL EN FORMATO LOCAL CON LA LOCALIZACION SETEADA EN ESPAÑOL
print('########################################################################################################################')

########################################################################################################################
#¿QUE ES UN TIMESTAMP?
# El timestamp mas utilizado es el numero de segundos que ha pasado desde el 1 de enero de 1970 GMT hasta el momento en que se ejecuta el programa.
# Nos sirve para identificar una fecha y hora exactas con un simple numero entero.
# Tambien se lo conoce como fecha 'Epoch' fecha UNIX o tiempo UNIX.
########################################################################################################################

#Obtener el timestamp de un objeto datetime (fecha)
hoy = dt_dt.today() # CREO LA VARIABLE hoy CON LA FECHA ACTUAL EN FORMATO DATETIME
timestamp = hoy.timestamp() # CREO LA VARIABLE timestamp CON EL TIMESTAMP DE LA FECHA ACTUAL
print(timestamp) # IMPRIMO EL TIMESTAMP DE LA FECHA ACTUAL

#Obtener el objeto fecha (datetime) de un timestamp
timestamp = 1588888888 # CREO LA VARIABLE timestamp CON EL TIMESTAMP QUE DESEO CONVERTIR A OBJETO DATETIME
fecha = dt_dt.fromtimestamp(timestamp) # CREO LA VARIABLE fecha CON EL OBJETO DATETIME DE LA FECHA QUE DESEO CONVERTIR
print(fecha) # IMPRIMO LA FECHA CON EL TIMESTAMP QUE DESEO CONVERTIR
print('########################################################################################################################')

########################################################################################################################
#Pasando a otro huso horario
########################################################################################################################

import pytz # IMPORTO LA LIBRERIA PYTZ PARA PODER CAMBIAR DE HUSO HORARIO
hoy = dt_dt.now() # CREO LA VARIABLE hoy CON LA FECHA ACTUAL EN FORMATO DATETIME
hoy_berlin = hoy.astimezone(pytz.timezone('Europe/Berlin')) # CREO LA VARIABLE hoy_berlin CON LA FECHA ACTUAL EN FORMATO DATETIME EN EL HUSO HORARIO DE BERLIN
print('La fecha y hora local es:', hoy) # IMPRIMO LA HORA ACTUAL EN FORMATO DATETIME
print('La fecha y hora en Berlin es:', hoy_berlin) # IMPRIMO LA HORA ACTUAL EN FORMATO DATETIME EN EL HUSO HORARIO DE BERLIN
#print('La diferencia de horas entre Berlin y local es:', hoy_berlin - hoy) !ERROR TypeError: can't subtract offset-naive and offset-aware datetimes
print('Las timezones son:', pytz.all_timezones) # IMPRIMO TODAS LAS TIMEZONES
print('########################################################################################################################')

########################################################################################################################
#JUGANDO CON CALENDARIOS
########################################################################################################################

import calendar # IMPORTO LA LIBRERIA CALENDAR PARA PODER HACER CALCULOS CON LOS CALENDARIOS
año = 2021 # CREO LA VARIABLE año CON EL AÑO QUE DESEO CALCULAR
separacion_horiz = 1
separacion_vert = 1
calle = 3
meses_por_fila = 3
calendar.prcal(año, separacion_horiz, separacion_vert, calle, meses_por_fila) # IMPRIMO EL CALENDARIO DEL AÑO QUE DESEO CALCULAR
print('########################################################################################################################')
mes = 3
calendar.prmonth(año, mes) # IMPRIMO EL CALENDARIO DEL MES QUE DESEO CALCULAR
print('########################################################################################################################')
print(calendar.isleap(año)) # IMPRIMO SI EL AÑO QUE DESEO CALCULAR ES BISIESTO
print('########################################################################################################################')
print(calendar.leapdays(2020, 2035)) # IMPRIMO LA CANTIDAD DE DIAS/AÑOS BISIESTOS ENTRE LOS AÑOS 2020 Y 2035
print('########################################################################################################################')
#IMPRIMO EL DIA DE LA SEMANA EN EL QUE CAERA UNA FECHA 0=lunes, 1=martes, 2=miercoles, 3=jueves, 4=viernes, 5=sabado, 6=domingo
dia = calendar.weekday(2021, 3, 1) # IMPRIMO EL DIA DE LA SEMANA EN EL QUE CAERA EL 1 DE ENERO DEL AÑO QUE DESEO CALCULAR
print(dia)
print('########################################################################################################################')
import locale
locale.setlocale(locale.LC_TIME, 'en') # SETEO LA LOCALIZACION DE LA FECHA EN FORMATO LOCAL EN INGLES
print(calendar.day_name[dia]) # IMPRIMO EL DIA DE LA SEMANA EN EL QUE CAERA EL 1 DE ENERO DEL AÑO 2021 EN FORMATO LOCAL EN INGLES

locale.setlocale(locale.LC_TIME, 'es') # SETEO LA LOCALIZACION DE LA FECHA EN FORMATO LOCAL EN ESPAÑOL
print(calendar.day_name[dia]) # IMPRIMO EL DIA DE LA SEMANA EN EL QUE CAERA EL 1 DE ENERO DEL AÑO 2021 EN FORMATO LOCAL EN ESPAÑOL
print('########################################################################################################################')

#Funcion Monthrange - devuelve el numero de dia (lunes=0...domingo=6) y el numero de dias del mes
print(calendar.monthrange(2021, 3)) # IMPRIMO EL NUMERO DE DIA Y EL NUMERO DE DIAS DEL MES DE MARZO DE 2021