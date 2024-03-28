class Batalla:
    def __init__(self, tiempo, peso):
        self.tiempo = tiempo
        self.peso = peso

    def optimizar_batallas(lista_batallas):
        lista_batallas.sort(key=lambda x: (x.peso/x.tiempo) ,reverse=True)

        suma,tiempo = 0,0
        for b in lista_batallas:
            tiempo += b.tiempo
            suma += tiempo * b.peso

        return lista_batallas, suma