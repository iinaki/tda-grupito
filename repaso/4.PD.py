from grafo import Grafo

def camino_mas_largo(grafo, vertices):
    OPT = {v: 0 for v in vertices}
    v_entrantes = {v: set() for v in vertices}
    for v in vertices:
        for w in grafo.adyacentes(v):
            v_entrantes[w].add(v)

    #ecuación
    for v in vertices:
        max = 0
        for w in v_entrantes[v]:
            if OPT[w] > max:
                max = OPT[w]
        OPT[v] = max + 1
        if len(v_entrantes[v]) == 0:
            OPT[v] = 0

    #reconstrucción
    camino = []
    actual = vertices[-1]
    camino.append(actual)
    for i in range(OPT[vertices[-1]]):
        for v in v_entrantes[actual]:
            if OPT[v] == OPT[actual] - 1:
                actual = v
                camino.append(actual)
                continue
    camino.reverse()
    return OPT, camino

grafo = Grafo(es_dirigido=True, vertices_init=['v1', 'v2', 'v3', 'v4', 'v5'])
grafo.agregar_arista('v1', 'v2')
grafo.agregar_arista('v1', 'v4')
grafo.agregar_arista('v2', 'v4')
grafo.agregar_arista('v2', 'v5')
grafo.agregar_arista('v3', 'v4')
grafo.agregar_arista('v4', 'v5')

# Lista de vértices en orden
vertices = ['v1', 'v2', 'v3', 'v4', 'v5']

# Calcular el camino más largo
opt, camino = camino_mas_largo(grafo, vertices)

print("Longitudes óptimas de caminos desde cada vértice:")
for v in vertices:
    print(f"{v}: {opt[v]}")

print("\nCamino más largo:")
print(" -> ".join(camino)) 

