#pip install pulp
import pulp
from backtracking import sumatoria
from leer_prueba import leer_prueba

# El objetivo es minimizar la diferencia del grupo de mayor suma con el de menor suma. En este caso, la solución será una aproximación al resultado óptimo.

def min_sumatoria_LP(maestros, k):
    n = len(maestros)

    # ordenamos antes
    maestros = sorted(maestros, key=lambda x : x[1], reverse=True)
    
    prob = pulp.LpProblem("tribu del agua", pulp.LpMinimize)
    
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(k)), cat='Binary') # 1 si el maestro i esta en el grupo j, 0 si no
    suma_grupo = pulp.LpVariable.dicts("suma_grupo", (i for i in range(k)), lowBound=0, cat='Continuous') # suma de habilidades de los maestros en grupo j
    
    Z = pulp.LpVariable("Z", lowBound=0, cat='Continuous')
    Y = pulp.LpVariable("Y", lowBound=0, cat='Continuous')
    
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

    #solver = pulp.PULP_CBC_CMD(timeLimit=300, gapRel=0.01)
    
    solver = pulp.GLPK_CMD(timeLimit=600, options=['--tmlim', '600'])

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


file = "./pruebas/20_8.txt"
x = leer_prueba(file)
grupos, suma = min_sumatoria_LP(x[1:],x[0])
print("Grupos formados:")
for i, grupo in enumerate(grupos):
    print(f"Grupo {i}: {grupo}")
print(f"Coeficiente: {suma}")

# RESULTADOS
# 5_2 bien
# 6_3 bien
# 6_4 bien
# 8_3 bien
# 10_3 bien
# 10_5 355882 contra 355890 - empieza a afectar lo de Z - Y
# 10_10 tarda 5mins y bien
# 11_5 bien
# 14_3 bien
# 14_4 bien
# 14_6 tarda 3mins y bien
# 15_4 bien
# 15_6 tarda 5mins y 6377225 contra 6377309
# 17_5 tarda 5mins y bien
# 17_7 tarda 5mins y 11513230 contra 11515918
# 17_10
# 18_6
# 18_8
# 20_4
# 20_5
# 20_8