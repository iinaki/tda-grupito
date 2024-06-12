#pip install pulp
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


file = "./pruebas/17_7.txt"
x = leer_prueba(file)
start = time.time()
grupos, suma = min_sumatoria_LP(x[1:],x[0])
end = time.time()
duration = end - start
print("Grupos formados:")
for i, grupo in enumerate(grupos):
    print(f"Grupo {i}: {grupo}")
print(f"Coeficiente: {suma}")
print("Duracion: ", duration)

# RESULTADOS
# 5_2 0.08158564567565918 1894340
# 6_3 0.20613765716552734 1640690
# 6_4 0.29298973083496094 807418
# 8_3 0.23009133338928223 4298131
# 10_3 0.6412622928619385 385249
# 10_5 1.8556880950927734 355882
# 10_10 602.8272588253021 172295
# 11_5 2.2033679485321045 2906564
# 14_3 1.816063404083252 15659106
# 14_4 16.281233310699463 15292055
# 14_6 207.54047012329102 10694510
# 15_4 18.635557413101196 4311889
# 15_6 332.6746037006378 6378149
# 17_5 600.2777290344238 15974095
# 17_7 tarda 5mins y 11513230 contra 11515918
# 17_10
# 18_6
# 18_8
# 20_4
# 20_5
# 20_8