import unittest  # Importa el módulo unittest para realizar pruebas unitarias

from appointmentQueue import appointmentQueue  # Importa la clase appointmentQueue desde el módulo appointmentQueue

class TestAppointmentQueue(unittest.TestCase):  # Define una nueva clase de prueba llamada TestAppointmentQueue que hereda de unittest.TestCase

    def setUp(self):  # Define el método setUp para configurar el entorno de prueba antes de cada prueba
        self.queue = appointmentQueue()  # Crea una instancia de la clase appointmentQueue para cada prueba
        # Define algunos datos de citas para usar en las pruebas
        self.data1 = {"userName": "Juan", "pharmacyName": "Farmacia A", "date": "2024-05-24", "hour": "10:00", "turn": 1}
        self.data2 = {"userName": "María", "pharmacyName": "Farmacia B", "date": "2024-05-25", "hour": "14:30", "turn": 2}
        self.data3 = {"userName": "Carlos", "pharmacyName": "Farmacia A", "date": "2024-05-26", "hour": "09:15", "turn": 3}

    def test_enqueue(self):  # Define el método de prueba test_enqueue para probar el encolado de citas
        self.queue.enqueue(self.data1)  # Agrega la primera cita a la cola
        self.queue.enqueue(self.data2)  # Agrega la segunda cita a la cola
        self.queue.enqueue(self.data3)  # Agrega la tercera cita a la cola
        # Verifica si el primer nodo (frente) de la cola contiene los datos de la primera cita y si el último nodo (final) contiene los datos de la tercera cita
        self.assertEqual(self.queue.front.data, self.data1)
        self.assertEqual(self.queue.rear.data, self.data3)

    def test_dequeue(self):  # Define el método de prueba test_dequeue para probar la desencolado de citas
        self.queue.enqueue(self.data1)  # Agrega la primera cita a la cola
        self.queue.enqueue(self.data2)  # Agrega la segunda cita a la cola
        self.queue.enqueue(self.data3)  # Agrega la tercera cita a la cola

        dequeued_data = self.queue.dequeue()  # Desencola la primera cita de la cola
        self.assertEqual(dequeued_data, self.data1)  # Verifica si los datos de la cita desencolada son los esperados
        self.assertEqual(self.queue.front.data, self.data2)  # Verifica si el frente de la cola ahora contiene los datos de la segunda cita
        # Desencola las siguientes citas y verifica si la cola se vacía correctamente
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertIsNone(self.queue.dequeue())  # Verifica si la cola está vacía después de desencolar todas las citas

    def test_is_empty(self):  # Define el método de prueba test_is_empty para probar si la cola está vacía
        self.assertTrue(self.queue.is_empty())  # Verifica si la cola está vacía inicialmente

        self.queue.enqueue(self.data1)  # Agrega una cita a la cola
        self.assertFalse(self.queue.is_empty())  # Verifica si la cola ya no está vacía después de agregar una cita

    def test_multiple_enqueues_and_dequeues(self):  # Define el método de prueba test_multiple_enqueues_and_dequeues para probar múltiples encolados y desencolados
        for i in range(1, 11):  # Itera sobre un rango de 1 a 10
            # Define datos de cita para cada iteración
            data = {"userName": f"Paciente {i}", "pharmacyName": f"Farmacia {i % 3}", "date": "2024-05-24", "hour": "10:00", "turn": i}
            self.queue.enqueue(data)  # Agrega la cita a la cola
        
        for i in range(1, 11):  # Itera sobre el mismo rango de 1 a 10
            dequeued_data = self.queue.dequeue()  # Desencola una cita de la cola
            # Define los datos esperados para la cita desencolada en cada iteración
            expected_data = {"userName": f"Paciente {i}", "pharmacyName": f"Farmacia {i % 3}", "date": "2024-05-24", "hour": "10:00", "turn": i}
            self.assertEqual(dequeued_data, expected_data)  # Verifica si los datos de la cita desencolada son los esperados
        
        self.assertTrue(self.queue.is_empty())  # Verifica si la cola está vacía después de desencolar todas las citas

if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente
    unittest.main()  # Ejecuta las pruebas unitarias
