# Trabajo Práctico 3: Problemas NP-Completos para la defensa de la Tribu del Agua

# Reglas de uso y como correr el TP

## Para ejecutar sobre un archivo específico
<!-- completar -->

## Para ejecutar pruebas
<!-- completar -->

### Ejemplo de ejecución
<!-- completar -->

## RESPUESTAS
1. Demostrar que el Problema de la Tribu del Agua se encuentra en NP.

Para demostrar que el Problema de la Tribu del Agua se encuentra en NP, debemos mostrar que una posible solución puede ser verificada en tiempo polinomial.
Entonces, tenemos que mostrar que dada una partición en k subgrupos  S_1, S_2, ... , S_k , podemos verificar en tiempo polinomial si esta partición cumple con la condición de que la adición de los cuadrados de las sumas de las fuerzas de los grupos es menor o igual que B.

Para verificar esto entonces el proceso que se tiene que seguir es:
- Para cada subgrupo S_i, calcular la suma de las fuerzas de los maestros en ese subgrupo. Es O(N) pq terminamos sumando todos los maestros.
- Elevar al cuadrado cada una de estas sumas. Es O(K) pq hay K subgrupos.
- Sumar estos cuadrados. También es O(K).
- Comparar el resultado con B para ver si cumple la condición. O(1)

Entonces la complejidad de la verificación es O( N + K + K + 1), y nos queda O( N + K ). Si sucede que K es mucho menor que N nos quedaría O(N).

Queda demostrado entonces que podemos verificar en tiempo polinomial si la propuesta de solución dada cumple o no, por lo tanto el Problema de la Tribu del Agua se encuentra en NP.

2. Demostrar que el Problema de la Tribu del Agua es, en efecto, un problema NP-Completo.

3. Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema

Realizamos un algoritmo de backtraking que obtiene la solución optima al problema de la mínima sumatoria. Generamos también sets de datos propios para corroborar el correcto funcionamiento del algoritmo y tomamos mediciones temporales.
Lo que hacemos en este algoritmo es probar todas las combinaciones diferentes de los maestros agua dados en K grupos que generan nuevas soluciones. Para evitar analizar combinaciones que no llegan a una solución óptima, fuimos generamos diferentes condiciones de corte en nuestro programa.

La función principal min_sumatoria se encarga de inicializar las estructuras necesarias y de llamar a la función recursiva _min_sum para realizar el backtracking. Creamos el grupo inicial de maestros que sale de ordenar de manera descendente a los maestros que recibimos, luego calculamos la sumatoria y la cota superior para el grupo inicial. 
<!-- pegar codigo -->

La función recursiva _min_sum realiza el proceso de backtracking, explora todas las posibles formas de distribuir a los maestros en los K grupos y recorta aquellas ramas que no pueden mejorar la solución actual. La parámetros que recibe la función son: "maestros", una lista de maestros agua con sus respectivas fuerzas, "grupos", una lista de un grupos de maestros, "n", el índice del maestro actual que se está evaluando, "sc", una lista con tres elementos: la mejor partición encontrada hasta el momento, la suma de los cuadrados de las sumas de las fuerzas de esa partición, y la cota superior de la partición, y por último "v_medio", valor medio de las fuerzas de los maestros. Luego de pasar por una serie de condicionees de corte llegamos a la parte del codigo donde el algoritmo intenta asignar el maestro actual a cada grupo a partir de un índice calculado para recortar las posibilidades de asignación. Añade el maestro al grupo, llama recursivamente a _min_sum para evaluar la siguiente asignación, y luego retira el maestro del grupo para probar la siguiente posibilidad. Si hemos asignado todos los maestros, es decir que n == len(maestros), evaluamos si la solución actual es mejor que la mejor encontrada hasta el momento. Si es así, actualizamos la mejor solución, la mejor sumatoria y la cota superior.
<!-- pegar codigo -->

Luego tenemos varias funciones auxiliares que nos ayudan a lograr el backtracking correctamente y a realizar podas.
- grupos_vacios: Cuenta el número de grupos vacíos.
- sumatoria: Calcula la suma de los cuadrados de las sumas de las fuerzas de los grupos.
- superanCotaSuperior: Verifica si algún grupo supera la cota superior.
- cota_superior: Calcula la cota superior de las fuerzas en los grupos.
- distribucion_inicial: Genera una distribución inicial de los maestros en los grupos.
<!-- pegar codigo -->

Condiciones de corte y optimizaciones
Gracias a las diferentes condiciones de corte y optimizaciones que le agregamos al algoritmos somos capaces de explorar muchas menos soluciones posibles, porque de esta manera nuestro algoritmo "se da cuenta" cuando esta llegando a una solucion que no es óptima.
Primero, antes de empezar con el algoritmo que resuelve el problema, ordenamos los maestros que recibimos segun sus niveles de habilidad en orden descendente, esto permite podar rapidamente las ramas de los valores muy altos. Luego en el algoritmo de backtracking tenemos un par de condiciones de corte muy básicas, que cortan si "n" es mayor que la cantidad de maestros, y si el número de grupos vacíos es mayor que la cantidad de maestros restantes, porque ahí no es posible llenar todos los grupos con los maestros restantes, por lo que se corta esta rama de búsqueda. Después nos fijamos si algún grupo supera la cota superior y luego vemos si la sumatoria parcial de las fuerzas de los grupos actuales es mayor o igual que la mejor sumatoria encontrada hasta ahora.


El algoritmo de backtracking desarrollado permite encontrar la partición óptima de los maestros agua en k subgrupos minimizando la suma de los cuadrados de las sumas de las fuerzas de los grupos. Garantizamos la solución óptima, aunque su complejidad es alta debido a la naturaleza del problema. Sin embargo las técnicas de poda de ramas nos ayuda a reducir significativamente el espacio de búsqueda, mejorando la eficiencia del algoritmo.
