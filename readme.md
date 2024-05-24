La complejidad temporal (notación Big O) de los métodos de la clase appointmentQueue es la siguiente:

enqueue(self, data): O(1) - Tiempo constante.

Esta operación simplemente crea un nuevo nodo y lo adjunta al final de la cola. Independientemente del tamaño de la cola, el número de operaciones permanece constante.
dequeue(self): O(1) - Tiempo constante.

Esta operación elimina y devuelve el nodo al frente de la cola. El tiempo que toma no depende del tamaño de la cola.
is_empty(self): O(1) - Tiempo constante.

Esta operación verifica si la cola está vacía verificando si el puntero front es None. Es una comparación única y rápida.

Complejidad temporal general:

Dado que todas las operaciones principales de esta implementación de cola (enqueue, dequeue, is_empty) toman un tiempo constante, la complejidad temporal general de la clase appointmentQueue es O(1).

Explicación:

La implementación de la cola utiliza una lista enlazada donde cada nodo (AppointmentNode) almacena los datos y una referencia (next) al siguiente nodo. Agregar o eliminar elementos del frente o del final de una lista enlazada se puede hacer en tiempo constante porque solo necesita manipular algunos punteros, independientemente de la cantidad de elementos en la lista.

Nota Importante:

La notación Big O se centra en el peor de los casos y en cómo el rendimiento del algoritmo escala con el tamaño de la entrada. En este caso, incluso si la cola tiene un millón de elementos, el tiempo necesario para enqueue, dequeue o verificar si está vacía seguirá siendo prácticamente el mismo.