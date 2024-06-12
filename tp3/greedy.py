import sys
import time
from leer_prueba import leer_prueba

def sumatoria(grupos):
    return sum(pow(sum(y for (x, y) in g), 2) for g in grupos)

#Aproximacion del Maestro Pakku
def greedy_aproximacion_de_pakku(maestros, k):
    grupos = [[] for _ in range(k)]
    maestros = sorted(maestros, key=lambda x: x[1], reverse=True)

    while (len(maestros) > 0):
        grupos.sort(key=lambda g: sum(y for (x, y) in g))
        grupos[0].append(maestros.pop(0))

    coef = sumatoria(grupos)

    return grupos, coef

#Nuestro algoritmo greedy
def greedy(maestros, k):
    grupos = [[] for _ in range(k)]

    maestros_copy = sorted(maestros, key=lambda x: x[1], reverse=True)
    while (len(maestros_copy) > 0):

        for i in range(k):
            if len(maestros_copy) > 0:
                grupos[i].append(maestros_copy.pop(0))

        for i in range(k):
            if len(maestros_copy) > 0:
                grupos[i].append(maestros_copy.pop())

    coef = sumatoria(grupos)

    return grupos, coef

if __name__ == '__main__':
    x = leer_prueba(sys.argv[1])

    start = time.time()
    grupos, coef = greedy_aproximacion_de_pakku(x[1:], x[0])
    end = time.time()

    print("Archivo: ", sys.argv[1])
    print("Duracion: ", end - start)
    print("GRUPOS:")
    for i, g in enumerate(grupos):
        print("GRUPO", i, g)
    print("Coeficiente: ", coef)