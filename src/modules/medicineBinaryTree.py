from datetime import datetime

class MedicineBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert_recursive(self.root, node)

    def _insert_recursive(self, current, node):
        expiry_date_current = datetime.strptime(current.expiryDate, "%Y-%m-%d")
        expiry_date_new = datetime.strptime(node.expiryDate, "%Y-%m-%d")
        
        if expiry_date_new < expiry_date_current:
            if current.left is None:
                current.left = node
            else:
                self._insert_recursive(current.left, node)
        else:
            if current.right is None:
                current.right = node
            else:
                self._insert_recursive(current.right, node)
       
    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node)
            self._inorder_traversal_recursive(node.right, result)