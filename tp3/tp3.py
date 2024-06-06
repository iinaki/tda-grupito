import os
import time
from backtracking import min_sumatoria
from leer_prueba import leer_prueba

start = time.time()
for file in os.listdir("./pruebas"):
    file = "./pruebas"+"/"+file

    x = leer_prueba(file)

    print("\n",file.name)
    grupos, coef = min_sumatoria(x[1:],x[0])
    print("GRUPOS:")
    for i, g in enumerate(grupos):
        print("GRUPO", i, g)
    print("Coeficiente:", coef)

end = time.time()
duration = end - start
print("Time: {} seconds".format(round(duration, 3)))