from patientNode import PatientNode  # Importa la clase PatientNode desde el módulo patientNode

class PatientQueue:  # Define una nueva clase llamada PatientQueue
    def __init__(self):  # Define el método inicializador (constructor) de la clase
        self.front = None  # Inicializa el puntero 'front' al frente de la cola como None
        self.rear = None   # Inicializa el puntero 'rear' al final de la cola como None

    def enqueue(self, data):  # Define el método para agregar un paciente a la cola
        # Crea un nuevo nodo de paciente con los datos proporcionados
        new_node = PatientNode(data)
        if self.is_empty():  # Verifica si la cola está vacía
            self.front = new_node  # Si está vacía, el nuevo nodo es tanto el frente como el final de la cola
            self.rear = new_node
        else:
            self.rear.next = new_node  # Enlaza el último nodo actual al nuevo nodo
            self.rear = new_node  # Actualiza el puntero 'rear' al nuevo nodo

    def dequeue(self):  # Define el método para quitar un paciente de la cola
        if self.is_empty():  # Verifica si la cola está vacía
            return None  # Si está vacía, no hay nada que quitar, retorna None
        else:
            dequeued_patient = self.front  # Almacena el nodo frontal en una variable temporal
            self.front = self.front.next  # Actualiza el frente al siguiente nodo en la cola
            if self.front is None:  # Si el frente es None después de la actualización, significa que la cola está vacía
                self.rear = None  # Actualiza el puntero 'rear' a None también
            return dequeued_patient.data  # Retorna los datos del paciente que fue eliminado de la cola

    def is_empty(self):  # Define el método para verificar si la cola está vacía
        return self.front is None  # Retorna True si el frente es None, lo que indica que la cola está vacía
