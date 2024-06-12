import os
import time
from backtracking import min_sumatoria
from greedy import greedy_aproximacion_de_pakku, greedy
from leer_prueba import leer_prueba

files = os.listdir("./pruebas")

def tiempos_algoritmo(algoritmo):
    tiempos = []

    for file in files:
        file = "./pruebas"+"/"+file

        x = leer_prueba(file)

        print("\n reading file: ",file)
        start = time.time()
        grupos, coef = algoritmo(x[1:],x[0])
        end = time.time()
        duration = end - start
        tiempos.append((file, duration, grupos, coef))

    return tiempos

def print_tiempos(algoritmo):
    tiempos_bck = tiempos_algoritmo(algoritmo)

    for t in tiempos:
        print("Archivo: ", t[0])
        print("Duracion: ", t[1])
        print("GRUPOS:")
        for i, g in enumerate(t[2]):
            print("GRUPO", i, g)
        print("Coeficiente: ", t[3])

print("TIEMPOS DE BACKTRACKING")
print_tiempos(min_sumatoria)

print("TIEMPOS DE GREEDY - APROXIMACION DE PAKKU")
print_tiempos(greedy_aproximacion_de_pakku)

print("TIEMPOS DE GREEDY - SOLUCION NUESTRA")
print_tiempos(greedy)