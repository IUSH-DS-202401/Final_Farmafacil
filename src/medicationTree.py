from medicationNode import MedicationNode  # Importa la clase MedicationNode desde el módulo medicationNode

class MedicationTree:  # Define una nueva clase llamada MedicationTree
    def __init__(self):  # Define el método inicializador (constructor) de la clase
        self.root = None  # Inicializa el atributo 'root' de la instancia a None, indicando que el árbol está vacío

    def insert(self, data):  # Define el método para insertar un nuevo nodo en el árbol
        self.root = self._insert_recursive(self.root, data)  # Llama al método de inserción recursiva

    def _insert_recursive(self, node, data):  # Define el método de inserción recursiva
        if node is None:  # Si el nodo actual es None, significa que hemos llegado a una hoja del árbol
            return MedicationNode(data)  # Crea un nuevo nodo con los datos proporcionados y devuélvelo como nodo insertado

        if data["units"] < node.data["units"]:  # Compara las unidades del nuevo dato con las unidades del nodo actual
            node.left = self._insert_recursive(node.left, data)  # Si las unidades son menores, inserta el nuevo dato en el subárbol izquierdo
        else:
            node.right = self._insert_recursive(node.right, data)  # Si las unidades son mayores o iguales, inserta el nuevo dato en el subárbol derecho
  
        return node  # Devuelve el nodo actual después de realizar la inserción

    def inorder_traversal(self):  # Define el método para realizar un recorrido en orden del árbol
        return self._inorder_recursive(self.root)  # Llama al método de recorrido en orden recursivo con la raíz del árbol

    def _inorder_recursive(self, node):  # Define el método de recorrido en orden recursivo
        elements = []  # Inicializa una lista para almacenar los elementos del recorrido en orden
        if node:  # Verifica si el nodo actual no es None
            elements.extend(self._inorder_recursive(node.left))  # Realiza un recorrido en orden del subárbol izquierdo
            elements.append(node.data)  # Agrega los datos del nodo actual a la lista
            elements.extend(self._inorder_recursive(node.right))  # Realiza un recorrido en orden del subárbol derecho
        return elements  # Devuelve la lista de elementos del recorrido en orden
    
    def print_tree(self):  # Define el método para imprimir el árbol en orden
        elements = self.inorder_traversal()  # Realiza un recorrido en orden para obtener los elementos del árbol
        for element in elements:  # Itera sobre cada elemento en el recorrido en orden
            print(element)  # Imprime el elemento (los datos del medicamento)
