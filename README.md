# Solución del juego Puzzle 8 por medio del algoritmo A*

El objetivo del rompecabezas es reorganizar las fichas en el estado inicial para que coincidan con el estado objetivo. El programa imprime la secuencia de movimientos para resolver el rompecabezas y alguna información adicional sobre la solución.

## Instrucciones de uso.

- Clona este repositorio en tu máquina local.
- Asegure que el respositorio se haya descargado correctamente.
- Abre el programa que deseas ejecutar en tu entorno de desarrollo que soporte Python 3.11.2 64-bit.

## Funcionamiento.

El juego de 8 es un rompecabezas clásico que implica mover piezas numeradas en un tablero de 3x3 para alcanzar el objetivo de encontrar una secuencia de movimientos que resuelva el rompecabezas desde una configuración inicial dada hasta el objetivo, el objetivo más común para este juego es la de ordenar de manera ascendente empezando desde la parte superior izquierda del tablero como se muestra en la `Imagen 1`.

<img src="/img/imagen6.png" alt="objetivoComunJuego8" title="Objetivo común en el juego del 8" width="500px"/>

> _**Imagen 1.- Objetivo común en el juego del 8**_

<br/>

El programa usa el orden de la `Imagen 2` como el tablero objetivo y el orden para mover las fichas será en el siguiente orden: Arriba, abajo, izquierda y derecha. Solo se pueden realizar movimientos válidos, es decir, mover una ficha adyacente al espacio vacío y siguiendo el orden de prioridad de movimientos ya mencionada y no se pueden realizar movimientos diagonales ni fuera de los límites del tablero.

<img src="/img/imagen2.png" alt="ordenTableroObjetivo" title="Orden para el tablero objetivo" width="250px"/>

> _**Imagen 2.- Orden para el tablero objetivo que se usó**_

Primero se define el tablero inicial que va a resolver (esta se define dentro del código), se define cuáles son los estados del problema, donde cada uno de los estados del problema pueda ser esquematizado gráficamente y representado en forma simbólica que a su vez, cada estado debe ser capaz de realizar una transición de estado, es decir, que pueda ser capaz de cambiar a otro estado y de esta manera se define un espacio de estados (o búsqueda) de un problema dado, esto representa un grafo, o alguna estructura de datos similar, cuyos nodos representan las configuraciones que puedan ser alcanzadas (los estados válidos) y las conexiones son las movidas posibles que pueda tener cada estado (transición de estado). De esta manera un estado en el juego pueda ser presentado como en la `Imagen 1`, puesto que una transición de estado es la transformación de un estado a otro estado, como se muestra en la `Figura 1`, y un espacio de estados son todas las posibles transiciones que puedan realizarse de un estado a otros, la `Figura 2` muestra, con una estructura de árbol, un conjunto de estados.

<img src="/img/figura1.png" alt="transicionEstado" title="Transición de un estado" width="300px"/>

> _**Figura 1.- Transición de un estado**_

<img src="/img/figura2.jpg" alt="arbolAlgunosPosiblesEstados" title="Árbol de algunos posibles estados" width="600px"/>

> _**Figura 2.- Árbol de algunos posibles estados**_

Como el algoritmo A* es un método de búsqueda que se caracteriza por explorar un árbol o grafo de búsqueda desde el nodo de inicio hacia el nodo objetivo que, a diferencia de otras estrategias de búsqueda, emplea una heurística para guiar la exploración y evalúa cada nodo en función de su costo real acumulado y una estimación del costo restante para llegar al nodo objetivo, como muestra la `Figura 4` la cual es un árbol de búsqueda para la generación de los estados y la manera en que estos son accesados.

<img src="/img/figura3.png" alt="comportamientoArbolA" title="Comportamiento de un árbol A*" width="600px"/>

> _**Figura 3.- Comportamiento de un árbol A***_

## Ejecución.

<img src="/img/ejecucion.png" alt="ejecucionPrograma" title="Ejecución del programa" width="650px"/>

> _**Imagen 3.- Ejecucón del programa**_

## Notas.

- Siéntete libre de personalizar los estados inicial y objetivo para probar el guión con diferentes escenarios de 8 rompecabezas.
- Si hay problemas para encontrar una solución, puede deberse a limitaciones en el algoritmo de búsqueda A* con la heurística de distancia de Manhattan.
- Este código no tiene dependencias externas y debería funcionar con cualquier entorno Python 3.x.

Si deseas contribuir a este proyecto, puedes enviar solicitudes de extracción (pull requests) con mejoras o características adicionales y si tienes alguna pregunta o problema, puedes contactarme a través de mi perfil de GitHub MrMike92. :turtle:
