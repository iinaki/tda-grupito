import os
from leer_prueba import leer_prueba
from main import defensa_optima
from main import reconstruccion

set_pruebas = "./set_pruebas"

coeficiente_esperado = [2118,7492,4508,1237,1027749,11603,4230,825776,1167532,2321418,3087557,1424488,4400750,1413,3994,15842,504220]

i = 0

for file in os.listdir(set_pruebas):
    if file == "Resultados Esperados.txt":
        continue
    prueba = file
    file = set_pruebas + "/" + file 
    
    n, x, f = leer_prueba(file)
    OPT = defensa_optima(x, f, n)
    reco, max_bajas = reconstruccion(OPT, n)

    print("Prueba: " + prueba )
    if max_bajas == coeficiente_esperado[i]:
        print("\t...CORRECTA" + " el numero de bajas máximo es " + str(max_bajas))
    else:
        print("\t...ERRONEA")
    i += 1