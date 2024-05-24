from appointmentNode import AppointmentNode  # Importa la clase AppointmentNode desde el módulo appointmentNode

class appointmentQueue:  # Define una nueva clase llamada appointmentQueue
    def __init__(self):  # Define el método inicializador (constructor) de la clase
        self.front = None  # Inicializa el atributo 'front' a None, indicando que la cola está vacía
        self.rear = None   # Inicializa el atributo 'rear' a None, indicando que la cola está vacía

    def enqueue(self, data):  # Define el método 'enqueue' para agregar un elemento a la cola
        new_node = AppointmentNode(data)  # Crea una nueva instancia de AppointmentNode con el dato proporcionado
        if self.is_empty():  # Verifica si la cola está vacía
            self.front = new_node  # Si está vacía, el nuevo nodo es tanto el frente como la parte trasera de la cola
            self.rear = new_node
        else:  # Si la cola no está vacía
            self.rear.next = new_node  # Enlaza el último nodo actual al nuevo nodo
            self.rear = new_node  # Actualiza la parte trasera de la cola al nuevo nodo

    def dequeue(self):  # Define el método 'dequeue' para eliminar un elemento de la cola
        if self.is_empty():  # Verifica si la cola está vacía
            return None  # Si está vacía, no hay nada que devolver, retorna None
        else:  # Si la cola no está vacía
            dequeued_patient = self.front  # Almacena el nodo frontal en una variable temporal
            self.front = self.front.next  # Actualiza el frente al siguiente nodo en la cola
            if self.front is None:  # Si el frente es None después de la actualización, significa que la cola está vacía
                self.rear = None  # Actualiza la parte trasera a None también
            return dequeued_patient.data  # Retorna el dato del nodo que fue eliminado de la cola

    def is_empty(self):  # Define el método 'is_empty' para verificar si la cola está vacía
        return self.front is None  # Retorna True si el frente es None, lo que indica que la cola está vacía
