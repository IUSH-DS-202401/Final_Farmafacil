Proyecto Farmafácil

Documentación del Proyecto de Desarrollo de Software

Descripción General del Proyecto:

El proyecto consiste en el desarrollo de un software para la gestión de farmacias, permitiendo a los usuarios registrar información relacionada con la farmacia, pacientes y administradores. El sistema proporcionará autenticación y diferentes funcionalidades según el tipo de usuario.

 Funcionalidades Principales:

1. Autenticación:
   - Los usuarios pueden acceder al sistema como farmacia, paciente o administrador.

2. Opciones del Administrador:
   - Actualización de información de pacientes o de la farmacia.

3. Opciones del Paciente:
   - Solicitud de turnos.
   - Actualización de datos personales.
   - Búsqueda de farmacias o medicamentos.

4. Opciones de la Farmacia:
   - Gestión del inventario de medicamentos (inclusión y actualización).
   - Visualización de información de medicamentos.


 Estructura del Código:

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

 Módulos y Estructuras de Datos:

1. Pila:
   - Se utiliza una pila para almacenar usuarios.
   - Métodos: constructor, `size()` para obtener la longitud, `push()` para añadir un elemento, `pop()` para eliminar un elemento.

2. Árbol:
   - Se utiliza un árbol para almacenar información sobre medicamentos en la farmacia.
   - Los datos se insertan en orden de expiración para medicamentos.
   - Se utiliza un criterio alfabético ascendente para la inserción de datos de farmacias.

Con esta guía y documentación,  pueden entender la estructura del proyecto, las funcionalidades principales, la estructura del código y las estructuras de datos utilizadas. Esto facilita el desarrollo, mantenimiento y comprensión del software.


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

