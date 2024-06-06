#pip install pulp
import pulp
from backtracking import sumatoria

# El objetivo es minimizar la diferencia del grupo de mayor suma con el de menor suma. En este caso, la solución será una aproximación al resultado óptimo.

def min_sumatoria_LP(maestros, k):
    n = len(maestros)
    
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
    
    prob.solve()
    
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

maestros = [("aa",3), ("bb",6), ("cc",7), ("dd",2), ("ee",5), ("ff",9), ("gg",1), ("hh",8)]
k = 3
grupos, suma = min_sumatoria_LP(maestros, k)

print("Grupos formados:")
for i, grupo in enumerate(grupos):
    print(f"Grupo {i+1}: {grupo}")
    print(f"Suma de habilidades: {suma}")

