import unittest  # Importa el módulo unittest para realizar pruebas unitarias

from pharmacyStack import PharmacyStack  # Importa la clase PharmacyStack desde el módulo pharmacyStack

class TestPharmacyStack(unittest.TestCase):  # Define una nueva clase de prueba llamada TestPharmacyStack que hereda de unittest.TestCase
    
    def setUp(self):  # Define el método setUp para configurar el entorno de prueba antes de cada prueba
        self.pharmacy_stack = PharmacyStack()  # Crea una instancia de la clase PharmacyStack para cada prueba
        # Define algunos datos de farmacia para usar en las pruebas
        self.pharmacy_data1 = {
            "name": '1',
            "tax_id": '1',
            "password": '1',
            "phone": '1',
            "address": '1',
            "admin_name": '1',
            "admin_id": '1',
        }
        self.pharmacy_data2 = {
            "name": '2',
            "tax_id": '2',
            "password": '2',
            "phone": '2',
            "address": '2',
            "admin_name": '2',
            "admin_id": '2',
        }
        self.pharmacy_data3 = {
            "name": '3',
            "tax_id": '3',
            "password": '3',
            "phone": '3',
            "address": '3',
            "admin_name": '3',
            "admin_id": '3',
        }

    def test_push(self):  # Define el método de prueba test_push para probar el apilado de farmacias
        self.pharmacy_stack.push(self.pharmacy_data1)  # Apila el primer conjunto de datos de farmacia
        self.pharmacy_stack.push(self.pharmacy_data2)  # Apila el segundo conjunto de datos de farmacia
        # Verifica si la parte superior de la pila contiene los datos de la segunda farmacia
        self.assertEqual(self.pharmacy_stack.top.data, self.pharmacy_data2)

    def test_pop(self):  # Define el método de prueba test_pop para probar el desapilado de farmacias
        self.pharmacy_stack.push(self.pharmacy_data1)  # Apila el primer conjunto de datos de farmacia
        self.pharmacy_stack.push(self.pharmacy_data2)  # Apila el segundo conjunto de datos de farmacia
        self.pharmacy_stack.push(self.pharmacy_data3)  # Apila el tercer conjunto de datos de farmacia
        
        popped_pharmacy = self.pharmacy_stack.pop()  # Desapila el elemento superior de la pila
        # Verifica si los datos desapilados corresponden al tercer conjunto de datos de farmacia
        self.assertEqual(popped_pharmacy, self.pharmacy_data3)
        # Verifica si la parte superior de la pila ahora contiene los datos del segundo conjunto de datos de farmacia
        self.assertEqual(self.pharmacy_stack.top.data, self.pharmacy_data2)

    def test_peek(self):  # Define el método de prueba test_peek para probar la visualización del elemento superior de la pila
        self.pharmacy_stack.push(self.pharmacy_data1)  # Apila el primer conjunto de datos de farmacia
        self.pharmacy_stack.push(self.pharmacy_data2)  # Apila el segundo conjunto de datos de farmacia
        # Verifica si la visualización del elemento superior de la pila devuelve los datos del segundo conjunto de datos de farmacia
        self.assertEqual(self.pharmacy_stack.peek(), self.pharmacy_data2)

    def test_is_empty(self):  # Define el método de prueba test_is_empty para probar si la pila está vacía
        # Verifica si la pila está vacía inicialmente
        self.assertTrue(self.pharmacy_stack.is_empty())

if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente
    unittest.main()  # Ejecuta las pruebas unitarias
