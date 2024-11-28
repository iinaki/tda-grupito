def verificar_hitting_set(A, subconjuntos, k, C):
    A = set(A)

    for subconjunto in subconjuntos:
        if not set(subconjunto).issubset(A):
            return False
    
    if not set(C).issubset(A):
        return False
   
    if len(C) > k:
        return False
    
    for subconjunto in subconjuntos:
        if not any(elemento in C for elemento in subconjunto):
            return False
        
    return True

if __name__ == "__main__":

    A = {1, 2, 3, 4, 5}  # Elementos del conjunto A
    subconjuntos = [
        {1, 2},      # B1
        {2, 3},      # B2
        {3, 4},      # B3
        {4, 5},      # B4
    ]
    k = 2  

    C = {2, 4}  # Conjunto solución propuesto
    if verificar_hitting_set(A, subconjuntos, k, C):
        print("C es una solución válida para el Hitting Set Problem.")
    else:
        print("C NO es una solución válida para el Hitting Set Problem.")