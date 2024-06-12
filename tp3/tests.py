import os
import time
from backtracking import min_sumatoria
#from programacion_lineal import min_sumatoria_LP
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

def print_tiempos(tiempos):
    for t in tiempos:
        print("Archivo: ", t[0])
        print("Duracion: ", t[1])
        print("GRUPOS:")
        for i, g in enumerate(t[2]):
            print("GRUPO", i, g)
        print("Coeficiente: ", t[3])

tiempos_bck = tiempos_algoritmo(min_sumatoria)
#tiempos_LP = tiempos_algoritmo(min_sumatoria_LP)

print("TIEMPOS DE BACKTRACKING")
print_tiempos(tiempos_bck)

#print("TIEMPOS DE LP")
#print_tiempos(tiempos_LP)