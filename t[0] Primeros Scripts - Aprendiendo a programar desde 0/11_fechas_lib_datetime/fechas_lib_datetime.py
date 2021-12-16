# LIBRERIA DATETIME
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

#CONVERTIR UN STRING EN UN OBJETO DATETIME
hoy = dt_dt.today()
expiracion_str = '2022-03-01'
expiracion = dt_dt.strptime(expiracion_str, '%Y-%m-%d')
expiracion - hoy

# vencimiento = expiracion - hoy

# dt_dt.ctime(vencimiento)

# print('VENCIMIENTO: ', vencimiento)