from greedy import greedy_aproximacion_de_pakku

def min_sumatoria(maestros, k):

    grupos = [[] for _ in range(k)]

    #los ordeno para que se recorten los primeroas ramas con valores altos
    maestros = sorted(maestros, key=lambda x : x[1], reverse=True)

    grupo_inicial = distribucion_inicial(maestros.copy(),k)

    suma_total = sumatoria(grupo_inicial)

    cota_sup = cota_superior(grupo_inicial)

    sc = [grupo_inicial, suma_total, cota_sup]

    _min_sum(maestros, grupos, 0, sc)

    return sc[0], sc[1]

def _min_sum(maestros, grupos, n, sc):

    if n > len(maestros):
        return

    # si faltan colocar menos maestros que grupos vacios vuelve
    if grupos_vacios(grupos) > len(maestros) - n:
        return

    # si algun grupo supera la cota superior
    if superan_cota_superior(grupos,sc[2]):
        return

    # calculo la sumatoria parcial
    suma_parcial = sumatoria(grupos)

    # si mi sumatoria parcial es mayor vuelve
    if suma_parcial >= sc[1]:
        return

    # si ya use todos los maestros
    if n == len(maestros):
        # cambio si es mejor solucion
        if sumatoria(grupos) < sc[1]:
            sc[0] = [list(g) for g in grupos] #copia de array
            sc[1] = suma_parcial
            sc[2] = cota_superior(grupos) # actualizo la cota superior
        # si no vuelve
        return

    # Ordenar los grupos antes de añadir el siguiente maestro
    grupos.sort(key=lambda g: sum(y for (x, y) in g))

    # por cada grupo pruebo con el maestro actual o sin
    a = len(grupos)-1 - n if n <= len(grupos)-1 else 0 #recorte de posibilidades de primeros k grupos
    for g in grupos[a:]:
        g.append(maestros[n])
        _min_sum(maestros, grupos, n+1, sc)
        g.pop()

def grupos_vacios(grupos):
    return sum(1 for g in grupos if not g)

def sumatoria(grupos):
    return sum(pow(sum(y for (x, y) in g), 2) for g in grupos)

def superan_cota_superior(grupos, cota_sup):
    for g in grupos:
        if len(g) > 1 and sum(y for (x,y) in g) > cota_sup:
            return True
    return False

def cota_superior(grupos):
    grupo_max = max(grupos, key=lambda x : sum(y for (x, y) in x))
    return (sum(y for (x,y) in grupo_max))


