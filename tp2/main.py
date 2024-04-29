import sys
from leer_prueba import leer_prueba

def defensa_optima(x,f,n):
    if n == 0:
        return 0
    
    OPT = [[0] * (n+1) for _ in range(n+1)]
    
    for m in range(1, n+1):
        for j in range(1, m+1):
            OPT[m][j] = max(OPT[m][j-1], (OPT[m-j][m-j] + min(f[j], x[m])))

    return OPT

def reconstruccion(OPT, n):
    reco = []
    max_bajas = OPT[n][n]
    m, j = n,n
    while j != 0:
        if OPT[m][j] != OPT[m][j-1]:
            reco.insert(0, "ATACAR")
            for i in range(j-1):
                reco.insert(0, "CARGAR")
            m -= j
            j = m
        else:
            j -= 1

    return reco, max_bajas

def main():
    if len(sys.argv) != 2:
        print("El uso del programa es: python main.py archivo.txt")
        return

    archivo_prueba = sys.argv[1]

    n,x,f = leer_prueba(archivo_prueba)

    OPT = defensa_optima(x, f, n)
    reco, max_bajas = reconstruccion(OPT, n)


    print("Estrategia: ", reco)
    print("Cantidad de tropas eliminadas: ", max_bajas)

if __name__ == "__main__":
    main()
