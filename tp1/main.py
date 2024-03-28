from TDABatalla import Batalla

archivo_entrada = "entrada.txt"
archivo_salida = "salida.txt"

with open(archivo_entrada, "r") as f:
    batallas = []
    next(f)
    for line in f:
        ti, bi = line.split(",")
        batallas.append(Batalla(int(ti), int(bi)))

batallas, coeficiente = Batalla.optimizar_batallas(batallas)

with open(archivo_salida, "w") as f:
    s = "Coeficiente de batalla : " +  str(coeficiente)
    f.write(s)

    f.write("\nLista de batallas ordenada:")
    f.write("\nti, bi")
    for b in batallas:
        s = "\n" + str(b.tiempo) + "," + str(b.peso)
        f.write(s)