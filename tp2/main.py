from leer_prueba import leer_prueba


def algoritmo_llorens(x, f, n): #????
    if n == 0:
        return 0

    OPT_LLORENS = [0] * (n+1)

    OPT_LLORENS[0] = 0
    OPT_LLORENS[1] = f[1]
    for j in range (1, n+1):
        AUX_LLORENS = []
        for i in range(0, j+1):
            AUX_LLORENS.append(OPT_LLORENS[j-i]+min(f[i], x[j]))

        OPT_LLORENS[j] = max(AUX_LLORENS)

    return OPT_LLORENS[n]


def algoritmo_llorens2(x, f, n): #????
    if n == 0:
        return 0

    OPT_LLORENS = [[0] * (n+1) for _ in range(n+1)]
    OPT_LLORENS[1][1] = min(f[1],x[1])

    for j in range (2, n+1):
        for i in range(1, j+1):
            OPT_LLORENS[j][i] = (max(OPT_LLORENS[j-i]) + min(f[i], x[j]))

    return OPT_LLORENS

# def reconstruccion(OPT, n):
#     j = n
#     sol = []
#     max_actual = OPT[n]

#     while j >= 0:
#         for i in range(1, j+1):
#             if OPT[j][i] == max_actual:
#                 sol.append("ATACAR")
#                 max_actual = max(OPT[j-i])
#                 j = j - i
#                 for _ in range(0, i):
#                     sol.append("DESCANSAR")
#                 break

#     sol.reverse()

#     return sol

def reconstruccion_pacheco(OPT, n):
    reco = []
    reco.append("ATACAR")
    i = n-1
    while i>=0:
        fila = OPT[i]
        print(fila)
        j = fila.index(max(fila))
        print("j es ", j)
        for _ in range(j):
            reco.append("DESCANSAR")
        i = i-j
        print("reco es ", reco)
        print("i es ", i)

    return reco.reverse()
        


def main():
    n,x,f = leer_prueba('set_pruebas/5.txt')
    OPT = algoritmo_llorens2(x, f, n)
    print(OPT)
    #reco = reconstruccion_pacheco(OPT, n)
    #print(reco)
    # return reconstruccion(OPT, n)

main()


# n,x,f = leer_prueba('set_pruebas/10.txt')

#print("EN PRUEBA de 10: n es ", n," x es ", x, " f es ", f)
#print(algoritmo_llorens(x, f, n))
#print(algoritmo_llorens2(x, f, n))

#n,x,f = leer_prueba('set_pruebas/500.txt')

#print("EN PRUEBA de 500: n es ", n," x es ", x, " f es ", f)
#print(algoritmo_llorens(x, f, n))
#print(algoritmo_llorens2(x, f, n))

# n,x,f = leer_prueba('set_pruebas/5000.txt')

# # print("EN PRUEBA de 5000: n es ", n," x es ", x, " f es ", f)
# print(algoritmo_llorens(x, f, n))
# print(algoritmo_llorens2(x, f, n))