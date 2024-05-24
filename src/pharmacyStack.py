from pharmacyNode import PharmacyNode

class PharmacyStack:
    def __init__(self):
        self.top = None  

    def push(self, data):
        #Agrega un nuevo nodo a la cima de la pila.
        new_node = PharmacyNode(data) 
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        # Remueve y devuelve el nodo de la cima de la pila
        if self.is_empty():
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data  # Devolvemos los datos del nodo

    def peek(self):
        # Devuelve el nodo de la cima sin removerlo.
        return self.top.data if self.top else None

    def is_empty(self):
        # Verifica si la pila está vacía
        return self.top is None
