import pulp

# Crear el problema de maximización
problem = pulp.LpProblem("Maximize_e", pulp.LpMaximize)

# Definir las variables (enteras)
a = 100000  # a es una constante dada
b = pulp.LpVariable('b', lowBound=0, cat='Integer')
c = pulp.LpVariable('c', lowBound=0, cat='Integer')
d = pulp.LpVariable('d', lowBound=0, cat='Integer')
e = d  # e es igual a d

# Función objetivo
problem += e, "Maximize_e"

# Restricciones
problem += a + d == b + c, "Constraint_1"
problem += a + b == c + 2 * d, "Constraint_2"
problem += b >= c, "Constraint_3"
problem += c >= d, "Constraint_4"
problem += d >= 0, "Constraint_5"

# Resolver el problema
problem.solve()

# Mostrar los resultados
print(f"Estado: {pulp.LpStatus[problem.status]}")
print(f"b: {b.varValue}")
print(f"c: {c.varValue}")
print(f"d (e): {d.varValue}")
print(f"(a + d )** 2 - (b+c+e)**2: {(a + d.varValue) ** 2 - (b.varValue +c.varValue +e.varValue )**2}")