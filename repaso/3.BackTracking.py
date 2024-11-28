from grafo import Grafo
from vertice import Vertice

def _dominating_set(grafo, vertices, actual, solucion_parcial, suma_parcial, solucion_actual, suma_actual): 
    if es_dominating_set(grafo, solucion_parcial):
        if suma_actual < suma_parcial: 
           return solucion_actual, suma_actual
        else:
            return solucion_parcial[:], suma_parcial
    if actual >= len(vertices) or suma_parcial >= suma_actual:
        return solucion_actual, suma_actual
    solucion_parcial.append(vertices[actual])
    solucion_actual, suma_actual = _dominating_set(grafo, vertices, actual+1, solucion_parcial, suma_parcial + vertices[actual].valor, solucion_actual, suma_actual)
    solucion_parcial.pop()
    solucion_actual, suma_actual = _dominating_set(grafo, vertices, actual+1, solucion_parcial, suma_parcial + vertices[actual].valor, solucion_actual, suma_actual)
    return solucion_actual, suma_actual

def es_dominating_set(grafo, solucion):
    cubierto = set()
    for v in solucion:
        if v not in cubierto:
            cubierto.add(v)
        for w in grafo.adyacentes(v):
            if w not in cubierto:
                cubierto.add(w)
    return len(grafo) == len(cubierto)
    
def dominating_set(grafo):
    return _dominating_set(grafo, grafo.obtener_vertices(), 0, [], 0, None, float('inf'))

grafo = Grafo()

A = Vertice("A", 1)
B = Vertice("B", 2)
C = Vertice("C", 3)
D = Vertice("D", 4)

# Agregar los vértices al grafo
grafo.agregar_vertice(A)
grafo.agregar_vertice(B)
grafo.agregar_vertice(C)
grafo.agregar_vertice(D)

# Agregar las aristas
grafo.agregar_arista(A, B)
grafo.agregar_arista(A, C)
grafo.agregar_arista(B, D)

# Encontrar el Dominating Set
solucion, peso = dominating_set(grafo)

# Imprimir resultados
print("Dominating Set:", solucion)
print("Peso mínimo:", peso)