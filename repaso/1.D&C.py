def adelantos_ranking(lista):
    adelantos = {}
    for (player, _) in lista:
        adelantos[player] = 0
    merge_sort_modificado(lista, adelantos)
    return adelantos 

def merge_sort_modificado(arr, adelantos):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izq = merge_sort_modificado(arr[:medio], adelantos)
    der = merge_sort_modificado(arr[medio:], adelantos)
    return merge_conteo(izq, der, adelantos)

def merge_conteo(arr1, arr2, set_adelantos):
    i = 0
    j = 0
    nuevo = []
    while i < len(arr1) and j < len(arr2):

        if arr1[i][1] <= arr2[j][1]:
            nuevo.append(arr1[i])
            i += 1
        
        else: 
            nuevo.append(arr2[j])
            set_adelantos[arr1[i][0]] += len(arr1) - i
            j += 1
    nuevo.extend(arr1[i:])
    nuevo.extend(arr2[j:])
    return nuevo

#PRUEBA
#lista antes [(C, 2), (A, 3)), (B, 4),  (F, 5),  (E, 6),  (D, 8)]
lista = [("A", 3), ("B", 4), ("C", 2), ("D", 8), ("E", 6), ("F", 5)]
resultado = adelantos_ranking(lista)
print(resultado)
#RESULTADO ESPERADO:
#{'A': 1, 'B': 1, 'C': 0, 'D': 2, 'E': 1, 'F': 0}