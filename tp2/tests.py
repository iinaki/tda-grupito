import os
from leer_prueba import leer_prueba
from main import algoritmo_llorens2

set_pruebas = "./set_pruebas"

coeficiente_esperado = [2118,7492,4508,1237,11603,4230,1413,3994,15842,504220]
i = 0

for file in os.listdir(set_pruebas):
    prueba = file
    file = set_pruebas + "/" + file 
    
    n, x, f = leer_prueba(file)
    OPT = algoritmo_llorens2(x, f, n)
    coef = max(OPT[n])

    print("Prueba: " + prueba )
    if coef == coeficiente_esperado[i]:
        print("\t...CORRECTA" + " el numero de bajas máximo es " + str(coef))
    else:
        print("\t...ERRONEA")
    i += 1