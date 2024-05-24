import unittest  # Importa el módulo unittest para realizar pruebas unitarias

from medicationTree import MedicationTree  # Importa la clase MedicationTree desde el módulo medicationTree

class TestMedicationTree(unittest.TestCase):  # Define una clase de prueba llamada TestMedicationTree que hereda de unittest.TestCase

    def setUp(self):  # Define el método setUp para configurar el entorno de prueba antes de cada prueba
        self.tree = MedicationTree()  # Crea una instancia de la clase MedicationTree para cada prueba
        # Define algunos datos de medicamentos para usar en las pruebas
        self.data1 = {"name": "Medicamento A", "pharmacy": "Farmacia X", "batch_number": "12345", "expiration_date": "2025-12-31", "manufacturer": "Lab A", "units": 50}
        self.data2 = {"name": "Medicamento B", "pharmacy": "Farmacia Y", "batch_number": "67890", "expiration_date": "2024-06-30", "manufacturer": "Lab B", "units": 30}
        self.data3 = {"name": "Medicamento C", "pharmacy": "Farmacia Z", "batch_number": "54321", "expiration_date": "2026-03-15", "manufacturer": "Lab C", "units": 70}

    def test_insert(self):  # Define el método de prueba test_insert para probar la inserción de medicamentos en el árbol
        self.tree.insert(self.data1)  # Inserta el primer medicamento en el árbol
        self.tree.insert(self.data2)  # Inserta el segundo medicamento en el árbol
        self.tree.insert(self.data3)  # Inserta el tercer medicamento en el árbol

        # Verifica si los medicamentos se han insertado correctamente en el árbol
        self.assertEqual(self.tree.root.data, self.data1)
        self.assertEqual(self.tree.root.left.data, self.data2)
        self.assertEqual(self.tree.root.right.data, self.data3)

    def test_inorder_traversal(self):  # Define el método de prueba test_inorder_traversal para probar el recorrido en orden del árbol
        self.tree.insert(self.data1)  # Inserta el primer medicamento en el árbol
        self.tree.insert(self.data2)  # Inserta el segundo medicamento en el árbol
        self.tree.insert(self.data3)  # Inserta el tercer medicamento en el árbol

        expected_order = [self.data2, self.data1, self.data3]  # Define el orden esperado para el recorrido en orden
        # Verifica si el recorrido en orden del árbol coincide con el orden esperado
        self.assertEqual(self.tree.inorder_traversal(), expected_order)

    def test_empty_tree(self):  # Define el método de prueba test_empty_tree para probar un árbol vacío
        # Verifica si el árbol está vacío al principio y si el recorrido en orden del árbol vacío es una lista vacía
        self.assertIsNone(self.tree.root)
        self.assertEqual(self.tree.inorder_traversal(), [])
    
    def test_insert_duplicate_units(self):  # Define el método de prueba test_insert_duplicate_units para probar la inserción de medicamentos con unidades duplicadas
        # Define un nuevo medicamento con unidades duplicadas respecto al primer medicamento
        data4 = {"name": "Medicamento D", "pharmacy": "Farmacia W", "batch_number": "98765", "expiration_date": "2023-01-01", "manufacturer": "Lab D", "units": 50}
        self.tree.insert(self.data1)  # Inserta el primer medicamento en el árbol
        self.tree.insert(data4)  # Intenta insertar el nuevo medicamento en el árbol
        
        # Verifica si el primer medicamento se ha insertado correctamente en el árbol y si el nuevo medicamento se ha insertado como hijo derecho del primer medicamento
        self.assertEqual(self.tree.root.data, self.data1)
        self.assertEqual(self.tree.root.right.data, data4)  

if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente
    unittest.main()  # Ejecuta las pruebas unitarias
