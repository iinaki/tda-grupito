# Trabajo Práctico 1: Algoritmos Greedy en la Nación del Fuego

# Reglas de uso y como correr el TP

## Para uso normal

Para utilizar el programa se deben listar las batallas a ordenar en el archivo `entrada.txt` con el formato:
```sh
ti,bi
109,200
43,89
282,66
```

Sin dejar lineas en blanco. Luego ejecutar el archivo `main.py` y la salida sera entregada en el archivo `salida.txt`
con el mismo formato que el de la entrada, pero con las batallas ordenadas y ademas mostrando el coeficiente de batalla.


## Para ejecutar pruebas

Para agregar una nueva prueba al set de pruebas, se debe crear un nuevo archivo de texto con el formato mencionado anteriormente en la carpeta `set-prueba`.
Se debe agregar el resultado esperado por cada prueba al inicio de cada archivo. Se agrega de la siguiente manera: una linea que diga "resultado esperado:", seguida de otra linea con el coeficiente de batalla esperado. 

Para la ejecucion de todas las pruebas se debe correr el archivo `tests.py`, el cual mostrará por consola los resultados de cada prueba dependiendo de si cada set de prueba calculó correctamente su coeficiente.

### Ejemplo con el set de 10 elementos dado por la cátedra

```sh
resultado esperado:
309600
T_i,B_i
53,100
61,100
68,100
68,100
86,100
35,100
97,100
58,100
47,100
82,100
```


