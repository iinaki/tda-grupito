from grafo import Grafo

def dominating_set_arbol(g):
    grafo = g
    grados, hojas = obtener_grados_y_hojas(g)
    solucion = set()
    while hojas:
        hoja = hojas.pop()
        padre = obtener_padre(grafo, hoja)
        solucion.add(padre)
        for ady in grafo.adyacentes(padre):
            grados[ady] -= 1
            if grados[ady] == 1:
                hojas.add(ady)
            if grados[ady] == 0:
                hojas.discard(ady)
                grafo.borrar_vertice(ady) 
    return solucion

def obtener_grados_y_hojas(grafo):
    grados = {}
    hojas = set()
    for v in grafo.obtener_vertices():
        grados[v] = len(grafo.adyacentes(v))
        if grados[v] == 1:
            hojas.add(v)
    return grados, hojas

#funcion fea pero pa que se entienda mejor arriba
#es O(1) y solo la llamaremos para hojas
def obtener_padre(grafo, v):
    for w in grafo.adyacentes(v):
        return w




# Crear un grafo como ejemplo
grafo = Grafo()
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)
grafo.agregar_vertice(5)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(2, 5)

# Calcular el Dominating Set
dominating_set = dominating_set_arbol(grafo)
print("Dominating Set mínimo:", dominating_set)