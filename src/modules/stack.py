class Stack:
    def __init__(self):
        self.top = None  

    def is_empty(self):
        return self.top is None 
    
    
    def lenS(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top
            count = 0
            while current is not None:
                count += 1
                current = current.next
        
        return count
    
    def push(self, node):  
        new_node = node
        new_node.next = self.top  
        self.top = new_node  

    def pop(self):  
        if not self.is_empty():
            data = self.top.data  
            self.top = self.top.next  
            return data  
        else:
            raise IndexError("The stack is empty")

    def peek(self):  
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("The stack is empty")