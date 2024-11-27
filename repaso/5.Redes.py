from grafo import Grafo

def curz_roja(ambulancias, pedidos, distancias, k):
    grafo = modelar_grafo(ambulancias, pedidos, distancias, k)
    flujo = flujo(grafo, "s", "t")
    res = []
    for a in ambulancias:
        for p in pedidos:
            if grafo.estan_unidos(a, p) and flujo[(a, p)] == 1:
                res.append((a, p))
    if len(res) == len(pedidos):
        return True, res
    return False, []

def modelar_grafo(ambulancias, pedidos, distancias, k):
    grafo = Grafo(es_dirigido=True)
    grafo.agregar_vertice("s")
    grafo.agregar_vertice("t")

    for pedido in pedidos:
        grafo.agregar_vertice(pedido)
        grafo.agregar_arista(pedido, "t", 1)

    for ambulancia in ambulancias:
        grafo.agregar_vertice(ambulancia)
        grafo.agregar_arista("t", ambulancia, 1)
        for pedido in pedidos:
            if distancias[(ambulancia, pedido)] <= k:
                grafo.agregar_arista(ambulancia, pedido, 1)
    return grafo