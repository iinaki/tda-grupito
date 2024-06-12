#pip install pulp
import sys
import pulp
from backtracking import sumatoria
from leer_prueba import leer_prueba
import time

# El objetivo es minimizar la diferencia del grupo de mayor suma con el de menor suma. En este caso, la solución será una aproximación al resultado óptimo.

def min_sumatoria_LP(maestros, k):
    n = len(maestros)

    # ordenamos antes
    maestros = sorted(maestros, key=lambda x : x[1], reverse=True)
    
    prob = pulp.LpProblem("tribu del agua", pulp.LpMinimize)
    
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(k)), cat='Binary') # 1 si el maestro i esta en el grupo j, 0 si no
    suma_grupo = pulp.LpVariable.dicts("suma_grupo", (i for i in range(k)), lowBound=0, cat='Integer') # suma de habilidades de los maestros en grupo j
    
    Z = pulp.LpVariable("Z", lowBound=0, cat='Integer')
    Y = pulp.LpVariable("Y", lowBound=0, cat='Integer')
    
    prob += Z - Y
    
    for i in range(n):
        prob += pulp.lpSum(x[i, j] for j in range(k)) == 1
    
    for j in range(k):
        prob += suma_grupo[j] == pulp.lpSum(maestros[i][1] * x[i, j] for i in range(n))
    
    for j in range(k):
        prob += Z >= suma_grupo[j]
    
    for j in range(k):
        prob += Y <= suma_grupo[j]

    #hacer sudo apt-get install glpk-utils

    solver = pulp.PULP_CBC_CMD(timeLimit=600)
    
    #solver = pulp.GLPK_CMD(timeLimit=600, options=['--tmlim', '600'])

    prob.solve(solver)
    
    grupos = [[] for _ in range(k)]
    for i in range(n):
        for j in range(k):
            if pulp.value(x[i, j]) == 1:
                grupos[j].append(maestros[i])

    print(f"Mayor suma (Z): {pulp.value(Z)}")
    print(f"Menor suma (Y): {pulp.value(Y)}")
    print(f"Diferencia (Z - Y): {pulp.value(Z) - pulp.value(Y)}")

    suma = sumatoria(grupos)
    
    return grupos, suma

if __name__ == '__main__':
    x = leer_prueba(sys.argv[1])

    start = time.time()
    grupos, coef = min_sumatoria_LP(x[1:], x[0])
    end = time.time()

    print("Archivo: ", sys.argv[1])
    print("Duracion: ", end - start)
    print("GRUPOS:")
    for i, g in enumerate(grupos):
        print("GRUPO", i, g)
    print("Coeficiente: ", coef)