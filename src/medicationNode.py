class MedicationNode:  # Define una nueva clase llamada MedicationNode
    def __init__(self, data):  # Define el método inicializador (constructor) de la clase
        self.data = data  # Asigna el valor del parámetro 'data' al atributo 'data' del objeto
        self.left = None  # Inicializa el atributo 'left' del objeto a None, indicando que no hay nodo hijo izquierdo
        self.right = None  # Inicializa el atributo 'right' del objeto a None, indicando que no hay nodo hijo derecho
