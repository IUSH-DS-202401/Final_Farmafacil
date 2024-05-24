Proyecto Farmafacil


Documentación del Proyecto de Desarrollo de Software

Descripción General del Proyecto:

El proyecto consiste en una aplicación de software para la gestión integral de farmacias. La aplicación facilita el registro, seguimiento y administración eficiente de pacientes, medicamentos, inventario y citas médicas. Para optimizar el rendimiento y la organización de datos, se implementan estructuras de datos avanzadas como pilas (stacks), colas (queues) y árboles binarios (binary trees)
La tecnología subyacente, basada en estructuras de datos como pilas, colas y árboles binarios, garantiza un rendimiento óptimo y una experiencia de usuario fluida


 Funcionalidades Principales:

1.	Registro de pacientes
•	Se va a guardar el nombre 
•	La contraseña 
•	El celular 
•	La dirección 
•	Fecha de nacimiento 
•	Cuidad de residencia 


2.	 Registro de Farmacias
•	Nombre de la farmacia 
•	Nit
•	Contraseña
•	Celular
•	Dirección 
•	Administrador de la farmacia 
•	Cedula del administrador 


3.	Registro de Medicamentos 	
•	Nombre del medicamento 
•	Nombre de la farmacia 
•	Lote 
•	Fecha de expiración 
•	Fabricante 
•	Unidades Disponibles 


4.	Registro de citas 
•	Nombre del paciente 
•	Nombre de la farmacia 
•	Fecha de la cita 
•	Hora de la cita 
•	Turno 

5.	Consultas 
•	Consultar pacientes: Trae todos pacientes 
•	Consultar farmacias: Trae las farmacias 
•	Consultar Medicamentos: Trae los medicamentos registrados  
•	Consultar Citas: Trae todas las citas asignadas 


Módulos y Estructuras de Datos:

1.	Pila:
Una pila es una estructura de datos que sigue el principio "LIFO" (Last In, First Out), es decir, el último elemento que se agrega es el primero en salir.
              Se está utilizando la estructura de datos de pila para almacenar la información de las farmacias
	Aplicaciones al usar pilas:
a.	Gestión de memoria en la ejecución de programas
b.	Evaluación de expresiones y análisis sintáctico
c.	Algoritmos de búsqueda y recorrido
d.	Búsqueda en profundidad (DFS)
e.	Gestión de procesos en sistemas operativos
2.	Colas:
Una cola es una estructura de datos lineal que sigue el principio FIFO (First In, First Out), es decir, el primer elemento que entra es el primero en salir.
Se está utilizando para almacenar los pacientes y las citas.
Aplicaciones de las colas
a.	Algoritmos de búsqueda en amplitud (BFS)	
b.	Gestión de procesos
c.	Buffers de entrada/salida
3.	Árboles binarios:
Un árbol binario es una estructura de datos jerárquica en la que cada nodo tiene como máximo dos hijos, llamados hijo izquierdo e hijo derecho. El nodo principal se denomina raíz. Los nodos sin hijos se llaman hojas.
Terminología:
a.	Raíz (root): El nodo superior del árbol.
b.	Hijo (child): Un nodo directamente conectado a otro nodo cuando se mueve lejos de la raíz.
c.	Padre (parent): El nodo opuesto de un nodo hijo.
d.	Hoja (leaf): Un nodo sin hijos.
e.	Nivel (level): La distancia de un nodo a la raíz.
f.	Altura (height): El número de niveles en un árbol.

Tipos de árboles binarios:
1.	Árbol binario completo: Todos los niveles están completamente llenos, excepto posiblemente el último nivel, que se llena de izquierda a derecha.
2.	Árbol binario perfecto: Todos los niveles están completamente llenos.
3.	Árbol binario de búsqueda (BST): Los valores de los nodos izquierdos son menores que el valor del nodo padre, y los valores de los nodos derechos son mayores.
              Aplicaciones arboles:
1.	Almacenamiento y recuperación de datos
a.	BST
i.	Se utilizan para almacenar datos de manera ordenada, lo que permite búsquedas, inserciones y eliminaciones eficientes

b.	Árboles de expresión 
i.	Representan expresiones matemáticas para facilitar su evaluación y manipulación
c.	Algoritmos de decisión
d.	Árboles de decisión:
i.	Representan una serie de decisiones y sus posibles consecuencias para ayudar en la toma de decisiones.
e.	AI
i.	Árboles de juego: Representan posibles movimientos en juegos para ayudar a la IA a tomar decisiones estratégicas
f.	Criptografía
i.	Árboles de Merkle: Se utilizan para verificar la integridad de grandes conjuntos de datos de manera eficiente.
                                   

              
Esta notación Big O aplica para los módulos de las Citas y los pacientes considerando que se tiene la misma estructura lógica 

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


La complejidad temporal (notación Big O) de los métodos de la clase PharmacyStack es la siguiente:
push(self, data): O(1) - Tiempo constante.
Esta operación crea un nuevo nodo y lo coloca en la parte superior de la pila. Independientemente del tamaño de la pila, el número de operaciones permanece constante.
pop(self): O(1) - Tiempo constante.
Esta operación elimina y devuelve el nodo en la parte superior de la pila. El tiempo que toma no depende del tamaño de la pila.
peek(self): O(1) - Tiempo constante.
Esta operación devuelve el nodo en la parte superior de la pila sin eliminarlo. Es una operación rápida que no depende del tamaño de la pila.
is_empty(self): O(1) - Tiempo constante.



Esta operación verifica si la pila está vacía comprobando si el puntero top es None. Es una comparación simple y rápida.
Complejidad temporal general:
Dado que todas las operaciones principales de esta implementación de pila (push, pop, peek, is_empty) toman un tiempo constante, la complejidad temporal general de la clase PharmacyStack es O(1).

Explicación:
La implementación de la pila utiliza una lista enlazada donde cada nodo (PharmacyNode) almacena los datos y una referencia (next) al siguiente nodo. Agregar o eliminar elementos de la parte superior de una pila se puede hacer en tiempo constante porque solo necesita manipular unos pocos punteros, independientemente de la cantidad de elementos en la pila.

Nota importante:
La notación Big O se centra en el peor de los casos y en cómo el rendimiento del algoritmo escala con el tamaño de la entrada. En este caso, incluso si la pila tiene un millón de elementos, el tiempo necesario para push, pop, peek o verificar si está vacía seguirá siendo prácticamente el mismo.


La complejidad temporal (notación Big O) de los métodos de la clase MedicationTree depende de la estructura del árbol:

insert(self, data) y _insert_recursive(self, node, data):
Caso promedio: O(log n) - Tiempo logarítmico.
En un árbol binario de búsqueda balanceado, la inserción requiere atravesar el árbol desde la raíz hasta una hoja, lo que toma aproximadamente log₂n pasos, donde n es el número de nodos.
Peor caso: O(n) - Tiempo lineal.
Si el árbol está desequilibrado (por ejemplo, degenerado en una lista enlazada), la inserción puede requerir atravesar todos los nodos existentes.
inorder_traversal(self) y _inorder_recursive(self, node): O(n) - Tiempo lineal.
El recorrido inorden visita todos los nodos del árbol exactamente una vez.
print_tree(self): O(n) - Tiempo lineal.
Esta función realiza un recorrido inorden y luego imprime cada elemento, visitando todos los nodos una vez.

Explicación:
La implementación utiliza un árbol binario de búsqueda, donde los nodos se ordenan según el valor de "units" en sus datos. La inserción implica encontrar la posición correcta para el nuevo nodo basándose en esta ordenación, mientras que el recorrido inorden visita los nodos en orden ascendente de sus valores.

Consideraciones Importantes:
Equilibrio del árbol: La eficiencia de las operaciones de inserción y búsqueda en un árbol binario de búsqueda depende en gran medida de qué tan equilibrado esté el árbol. Un árbol balanceado mantiene una altura logarítmica, garantizando un rendimiento óptimo. Si el árbol se desequilibra, el peor de los casos se convierte en lineal, lo que reduce la eficiencia.

Casos de Uso Específicos: Si tienes garantías sobre cómo se insertarán los datos (por ejemplo, si los datos tienden a llegar en un orden aleatorio), es más probable que el árbol se mantenga equilibrado y el rendimiento promedio se acerque a O(log n) para la inserción.


 Estructura del Código usado para las ventanas 

1. Clase Screen:
   - La clase `Screen` establece las características fundamentales para crear una pantalla en la aplicación.
   - Esta clase sirve como base para la creación de otras pantallas en el sistema.
   - Constructor: `__init__(self, master=None)`.
     - Inicializa los elementos de la pantalla de Tkinter.
     - Almacena la referencia principal a la que pertenece la pantalla.
     - Establece el color de fondo de la pantalla.
     - Organiza y muestra la pantalla en la ventana principal.

2. Diseño de Pantallas:
   - Se utilizan widgets de Tkinter para diseñar las interfaces gráficas de usuario.
   - Se crean labels, se establecen propiedades como texto, fuente, color de fondo y color de primer plano.


Diagrama de Caso de Uso - Administrador

Descripción:

El Administrador puede autenticarse en el sistema.
Una vez autenticado, puede acceder a las opciones del Administrador, que incluyen la actualización de información de pacientes o de la farmacia.
Diagrama de Caso de Uso - Paciente

Descripción:

El Paciente puede autenticarse en el sistema.
Después de iniciar sesión, tiene acceso a las opciones del Paciente, como la solicitud de turnos, la actualización de datos personales y la búsqueda de farmacias o medicamentos.
Diagrama de Caso de Uso - Farmacia

Descripción:

La Farmacia puede autenticarse en el sistema.
Una vez autenticada, puede acceder a las opciones de la Farmacia, que incluyen la gestión del inventario de medicamentos (inclusión y actualización) y la visualización de información de medicamentos.


Inicio
    |
Autenticarse en el sistema
    |
¿Credenciales correctas? ---- No ----> Mostrar mensaje de error ----> Autenticarse en el sistema
    |
   Sí
    |
Acceder a opciones del Administrador
    |
Seleccionar acción ----> Actualizar información de pacientes ----> Introducir nueva información ----> Guardar cambios
                    |
                    ----> Actualizar información de la farmacia ----> Introducir nueva información ----> Guardar cambios
    |
Cerrar sesión
    |
Fin


Inicio
    |
Autenticarse en el sistema
    |
Credenciales correctas? ---- No ----> Mostrar mensaje de error ----> Autenticarse en el sistema
    |
   Sí
    |
Acceder a opciones del Paciente
    |
Seleccionar acción ----> Solicitar turnos ----> Introducir detalles del turno ----> Confirmar solicitud
                    |
                    ----> Actualizar datos personales ----> Introducir nueva información ----> Guardar cambios
                    |
                    ----> Buscar farmacias o medicamentos ----> Introducir criterios de búsqueda ----> Mostrar resultados
    |
Cerrar sesión
    |
Fin


Inicio
    |
Autenticarse en el sistema
    |
Credenciales correctas? ---- No ----> Mostrar mensaje de error ----> Autenticarse en el sistema
    |
   Sí
    |
Acceder a opciones de la Farmacia
    |
Seleccionar acción ----> Gestión del inventario de medicamentos ----> Incluir nuevo medicamento
                    |                                        |
                    |                                        ----> Actualizar información de medicamento existente
                    |
                    ----> Visualizar información de medicamentos ----> Mostrar lista de medicamentos
    |
Cerrar sesión
    |
Fin
