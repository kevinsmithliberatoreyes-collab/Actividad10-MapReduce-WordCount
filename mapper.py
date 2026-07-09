#!/usr/bin/env python3
import sys

# Iteramos de forma continua sobre cada línea de la entrada estándar (stdin)
for line in sys.stdin:
    # Eliminamos espacios en blanco al inicio y al final de la línea para evitar errores
    line = line.strip()
    # Dividimos la línea en un arreglo de palabras usando los espacios como separador
    words = line.split()
    # Iteramos sobre cada palabra encontrada en la línea procesada
    for word in words:
        # Imprimimos la palabra y el número 1 separados por un tabulador, 
        # que es el formato que Hadoop espera para la fase de Shuffle.
        print(f'{word}\t1')
