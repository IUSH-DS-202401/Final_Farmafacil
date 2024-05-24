from pharmacyStack import PharmacyStack  # Importa la clase PharmacyStack del módulo pharmacyStack
from patientQueue import PatientQueue  # Importa la clase PatientQueue del módulo patientQueue
from medicationTree import MedicationTree  # Importa la clase MedicationTree del módulo medicationTree
from appointmentQueue import appointmentQueue  # Importa la clase appointmentQueue del módulo appointmentQueue

# Crea instancias de las estructuras de datos para manejar las farmacias, pacientes, citas y medicamentos
pharmacy_stack = PharmacyStack()
patient_queue = PatientQueue()
appointment_queue = appointmentQueue()
medication_tree = MedicationTree()
turnCounter = 0  # Inicializa el contador de turnos a 0

def request_an_appointment():  # Define la función para solicitar una cita
    global turnCounter  # Permite modificar la variable global turnCounter
    turnCounter += 1  # Incrementa el contador de turnos
    
    # Solicita al usuario que ingrese los detalles de la cita
    userName = input("Enter your name: ")
    pharmacyName = input("Enter the pharmacy name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    hour = input("Enter the hour: ")
    
    # Crea un diccionario con los detalles de la cita
    appointmentBody = {
        "userName": userName,
        "pharmacyName": pharmacyName,
        "date": date,
        "hour": hour,
        "turn": turnCounter
    }
    
    appointment_queue.enqueue(appointmentBody)  # Encola la cita en la cola de citas
    
    print(userName + ' Your turn is ' + str(turnCounter))  # Informa al usuario de su turno

def register_pharmacy():  # Define la función para registrar una farmacia
    # Solicita al usuario que ingrese los detalles de la farmacia
    name = input("Enter the name: ")
    tax_id = input("Enter the tax ID (NIT): ")
    password = input("Enter the password: ")
    phone = input("Enter the phone number: ")
    address = input("Enter the address: ")
    admin_name = input("Enter the administrator's name: ")
    admin_id = input("Enter the administrator's ID (CC): ")
    
    # Crea un diccionario con los detalles de la farmacia
    pharmacyBody = {
        "name": name,
        "tax_id": tax_id,
        "password": password,
        "phone": phone,
        "address": address,
        "admin_name": admin_name,
        "admin_id": admin_id,
    }
    
    print(pharmacyBody)  # Muestra los detalles de la farmacia
    
    pharmacy_stack.push(pharmacyBody)  # Apila la farmacia en la pila de farmacias

def register_patient():  # Define la función para registrar un paciente
    # Solicita al usuario que ingrese los detalles del paciente
    name = input("Enter the name: ")
    patient_id = input("Enter the patient ID (CC): ")
    password = input("Enter the password: ")
    phone = input("Enter the phone number: ")
    address = input("Enter the address: ")
    birthdate = input("Enter the birthdate (YYYY-MM-DD): ")
    city = input("Enter the city of residence: ")
    
    # Crea un diccionario con los detalles del paciente
    patientBody = {
        "name": name,
        "patient_id": patient_id,
        "password": password,
        "phone": phone,
        "address": address,
        "birthdate": birthdate,
        "city": city
    }
    
    print(patientBody)  # Muestra los detalles del paciente
    
    patient_queue.enqueue(patientBody)  # Encola el paciente en la cola de pacientes

def register_medication():  # Define la función para registrar un medicamento
    # Solicita al usuario que ingrese los detalles del medicamento
    name = input("Enter the medication name: ")
    pharmacy = input("Enter the pharmacy name: ")
    batch_number = input("Enter the batch number: ")
    expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")
    manufacturer = input("Enter the manufacturer: ")
    units = int(input("Enter the number of units: "))
    
    # Crea un diccionario con los detalles del medicamento
    medicationBody = {
        "name": name,
        "pharmacy": pharmacy,
        "batch_number": batch_number,
        "expiration_date": expiration_date,
        "manufacturer": manufacturer,
        "units": units
    }
    
    print(medicationBody)  # Muestra los detalles del medicamento
    
    medication_tree.insert(medicationBody)  # Inserta el medicamento en el árbol de medicamentos

def get_pharmacies():  # Define la función para obtener todas las farmacias
    pharmacies = []  # Crea una lista vacía para almacenar las farmacias
    while not pharmacy_stack.is_empty():  # Mientras la pila de farmacias no esté vacía
        pharmacies.append(pharmacy_stack.pop())  # Extrae cada farmacia de la pila y la agrega a la lista
        
    print(pharmacies)  # Muestra todas las farmacias

def get_patients():  # Define la función para obtener todos los pacientes
    patients = []  # Crea una lista vacía para almacenar los pacientes
    while not patient_queue.is_empty():  # Mientras la cola de pacientes no esté vacía
        patients.append(patient_queue.dequeue())  # Extrae cada paciente de la cola y lo agrega a la lista
        
    print(patients)  # Muestra todos los pacientes

def get_medicines():  # Define la función para obtener todos los medicamentos
    medication_tree.print_tree()  # Imprime el árbol de medicamentos

def get_appointments():  # Define la función para obtener todas las citas
    appointments = []  # Crea una lista vacía para almacenar las citas
    while not appointment_queue.is_empty():  # Mientras la cola de citas no esté vacía
        appointments.append(appointment_queue.dequeue())  # Extrae cada cita de la cola y la agrega a la lista
        
    print(appointments)  # Muestra todas las citas

def closeApp():  # Define la función para cerrar la aplicación
    print("Closing app ...")  # Imprime un mensaje indicando que la aplicación se está cerrando
    exit()  # Termina la ejecución del programa

def main():  # Define la función principal
    while True:  # Bucle infinito para el menú principal
        # Muestra las opciones del menú al usuario
        print("\nChoose an action:")
        print("1. Register Pharmacy")
        print("2. Register Patient")
        print("3. Register Medication")
        print("4. Request an appointment")
        print("5. Get Pharmacies")
        print("6. Get Patients")
        print("7. Get Medicines")
        print("8. Get appointments")
        print("9. Exit")

        choice = input("Enter your choice: ")  # Solicita al usuario que ingrese una opción

        match choice:  # Estructura de control para manejar las diferentes opciones del menú
            case '1':
                register_pharmacy()
                
            case '2':
                register_patient()
                
            case '3':
                register_medication()
                
            case '4':
                request_an_appointment()
                
            case '5':
                get_pharmacies()
                
            case '6':
                get_patients()
                
            case '7':
                get_medicines()
                
            case '8':
                get_appointments()
                
            case '9':
                closeApp()
                
            case _:
                print("Invalid choice.")  # Mensaje para opciones no válidas

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    main()  # Llama a la función principal
