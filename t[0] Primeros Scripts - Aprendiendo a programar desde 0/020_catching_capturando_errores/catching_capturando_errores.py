# Ademas de salir por el except evitando el corte del script por un error,
# tambien podemos 'capturar' el error que salta en el try
# Para ello debemos importar la libreria sys
# En el bloque except capturamos el error usando el metodo exc_info() de la liberia sys

import sys

volumen = 1200
dias = 0

try:
    volMedio = volumen / dias
except:
    error = sys.exc_info()[1]
    print("Error detectado: ", error)

# Segundo ejemplo sin error

volumen = 1200
dias = 2
try:
    volMedio = volumen / dias
    print("El volumen medio es: ", volMedio)
except:
    error = sys.exc_info()[1]
    print("Error detectado: ", error)
