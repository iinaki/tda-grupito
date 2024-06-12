from backtracking import sumatoria

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
            if len(maestros) > 0:
                grupos[i].append(maestros_copy.pop())

    coef = sumatoria(grupos)

    return grupos, coef