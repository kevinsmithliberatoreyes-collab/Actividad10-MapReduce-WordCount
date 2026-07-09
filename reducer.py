#!/usr/bin/env python3
import sys

# Variables para llevar el control de la palabra actual y su sumatoria
current_word = None
current_count = 0

# Iteramos sobre cada línea que nos entrega la fase de Shuffle (que ya viene ordenada)
for line in sys.stdin:
    # Limpiamos los saltos de línea y espacios en blanco
    line = line.strip()
    # Separamos la clave (palabra) y el valor (conteo) por el tabulador
    word, count = line.split('\t', 1)
    
    # Convertimos el valor a un número entero. Si hay un error de formato, ignoramos la línea.
    try:
        count = int(count)
    except ValueError:
        continue
    
    # Si la palabra actual es igual a la que venimos arrastrando, acumulamos el valor
    if current_word == word:
        current_count += count
    else:
        # Si la palabra cambia y no es la primera iteración, imprimimos el total anterior
        if current_word:
            print(f'{current_word}\t{current_count}')
        # Reiniciamos las variables de control para la nueva palabra entrante
        current_word = word
        current_count = count

# Imprimimos la última palabra procesada al terminar de leer todo el flujo de datos
if current_word == word:
    print(f'{current_word}\t{current_count}')
