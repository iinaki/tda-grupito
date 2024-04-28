import sys
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

def reconstruccion(OPT, n):
    max_bajas = max(OPT[n])
    reco = []
    reco.insert(0,"ATACAR")
    i = n
    while i>0:
        fila = OPT[i]
        j = fila.index(max(fila))
        for _ in range(j-1):
            reco.insert(0,"DESCANSAR")
        if i-j<=0:
            return reco, max_bajas
        reco.insert(0, "ATACAR")
        i = i-j

    return reco, max_bajas
        


def main():
    if len(sys.argv) != 2:
        print("El uso del programa es: python main.py archivo.txt")
        return

    archivo_prueba = sys.argv[1]

    n,x,f = leer_prueba(archivo_prueba)

    OPT = algoritmo_llorens2(x, f, n)
    reco, max_bajas = reconstruccion(OPT, n)


    print("Estrategia: ", reco)
    print("Cantidad de tropas eliminadas: ", max_bajas)

if __name__ == "__main__":
    main()
