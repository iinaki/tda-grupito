def leer_prueba(path_prueba):
    x = []

    with open(path_prueba, 'r') as file:
        file.readline()
        n = int(file.readline().strip())
        x.append(n)
        for line in file.readlines():
            a = line.strip().split(',')
            x.append((a[0], int(a[1])))
    
    return x
