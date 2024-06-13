# Trabajo Práctico 3: Problemas NP-Completos para la defensa de la Tribu del Agua

# Reglas de uso y como correr el TP

## Para ejecutar sobre un archivo específico

Dividimos las soluciones de nuestro TP diferentes archivos para que el código quede más limpio y se pueda entender mejor. Tenemos las soluciones de backtracking, greedy y lineal en los archivos `backtracking.py`, `greedy.py` y `programacion_lineal.py`. Si se quiere obtener la solución para un problema con un método de resolución específico, se puede ejecutar en la terminal el siguiente comando, especificando el path al archivo al cual que se le quiere realizar el algoritmo:

- Para backtracking:
```sh
python backtracking.py pruebas/5_2.txt
```

- Para greedy, ejecuta la solución del maestro Pakku:
```sh
python greedy.py pruebas/5_2.txt
```

- Para programación lineal:
```sh
pip install pulp #si no se tiene instalado pulp para resolver con PL
python programacion_lineal.py pruebas/5_2.txt
```

El formato del archivo de test debe ser el mismo que el dado por las pruebas de la cátedra, es decir la primera línea es un comentario, luego la segunda indica la cantidad de grupos a formar. Luego vienen n líneas que corresponden a los maestros, cada maestro es una tupla de la forma `Nombre del maestro, nivel de poder`, por ejemplo:

```sh
# La primera linea indica la cantidad de grupos a formar, las siguientes son de la forma 'nombre maestro, habilidad'
2
Pakku, 101
Yue, 134
Yakone, 759
Pakku I, 308
Wei, 644
```

## Para ejecutar pruebas
Para agregar una nueva prueba al set de pruebas, se debe crear un nuevo archivo de texto con el formato mencionado anteriormente en la carpeta `pruebas`.

Para la ejecucion de todas las pruebas en el directorio `pruebas` se debe correr el archivo `tests.py`, el cual mostrará por consola los resultados de cada prueba resuelta con backtracking, y las dos soluciones greedy implementadas. Se puede correr de la siguiente manera:

```sh
python tests.py
```

Dejamos comentada la parte donde se ejecutan todas las pruebas con programación lineal, ya que hay muchas pruebas que tardan 10 minutos en correr, por lo que se puede hacer algo tediosa la ejecución. Sin embargo si se quieren correr todas las pruebas con PL, se puede descomentar la siguiente parte del código del archivo `tests.py`:

```sh
# SI SE QUIERE EJECUTAR LOS TESTS CON PLE, DESCOMENTAR ESTAS LINEAS
# print("TIEMPOS DE PROGRAMACION LINEAL")
# print_tiempos(min_sumatoria_LP)
```

