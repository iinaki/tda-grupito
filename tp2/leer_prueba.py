def leer_prueba(path_prueba):
    x = []
    f = []
    with open(path_prueba, 'r') as file:
        file.readline()
        n = int(file.readline().strip())

        for _ in range(n):
            x.append(int(file.readline().strip()))

        for _ in range(n):
            f.append(int(file.readline().strip()))

    return n, x, f