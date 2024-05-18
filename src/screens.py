import tkinter as tk
from tkinter import ttk
from db.patient import NodePatient
from db.pharmacy import NodePharmacy

class Screen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.resizable(False, False)
        self.config(bg='#E6F2FF')
        self.pack()
    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Farma Facil")
        self.geometry("700x350")
        self.current_screen = None
        self.show_screen(MainMenu)
    
    def show_screen(self, screen_class):
        new_screen = screen_class(self)
        if self.current_screen is not None:
            self.current_screen.destroy()
        self.current_screen = new_screen
        self.current_screen.pack()
        
class signUpSuccess(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Registro Exitoso", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)
        
        self.btnPharmacy = tk.Button(self.frame, text="Aceptar", command=self.go_to_main_menu, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)


class signIn(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Ingresar" , font=("Arial", 18, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.ccNit_label = tk.Label(self.frame, text="CC / NIT:", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.ccNit_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ccNit_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.ccNit_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        self.password_label = tk.Label(self.frame, text="Password:", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        self.btn_sign_in = tk.Button(self.frame, text="Ingresar", bg="#003366", fg="white", font=("Arial", 12, "bold"), width=17)
        self.btn_sign_in.grid(row=3, column=1, columnspan=2, pady=10)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)

class signInFailed(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="CC/Nit  o Contraseña Incorrectos", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)
        
        self.btnPharmacy = tk.Button(self.frame, text="Aceptar", command=self.go_to_main_menu, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
    
class signInSuccess(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Ingresó correctamente", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)
        
        self.btnPharmacy = tk.Button(self.frame, text="Aceptar", command=self.go_to_main_menu, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)


class signInAdmin(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Desea ingresar como", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnAdm = tk.Button(self.frame, text="Administrador", command=self.go_to_admin_menu, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnAdm.pack(pady=15)

        self.btnPatient = tk.Button(self.frame, text="Paciente", command=self.go_to_patient_menu, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPatient.pack(pady=15)
    
    def go_to_admin_menu(self):
        self.master.show_screen(AdminMenu)
    
    def go_to_patient_menu(self):
        self.master.show_screen(PatientMenu)
        
class AdminMenu(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menu Administrador", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Actualizar Adm/Paciente", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Actualizar Farmacia", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_update_user(self):
        self.master.show_screen(AdminUpdateUser)
    
    def go_to_update_pharmacy(self):
        self.master.show_screen(AdminUpdatePharmacy)
        
      
class AdminUpdatePharmacy(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x450")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Actualizar Farmacia" , font=("Arial", 18, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = tk.Label(self.frame, text="Nombre: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.name_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        self.nit_label = tk.Label(self.frame, text="Nit: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.nit_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.nit_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.nit_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        self.password_label = tk.Label(self.frame, text="Contraseña: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        self.phone_label = tk.Label(self.frame, text="Teléfono: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.phone_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.phone_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        self.address_label = tk.Label(self.frame, text="Dirección: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.address_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.address_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        self.adm_label = tk.Label(self.frame, text="Administrador: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.adm_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.adm_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.adm_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        self.cc_adm_label = tk.Label(self.frame, text="CC Administrador: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.cc_adm_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.cc_adm_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.cc_adm_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
            
        self.btn_update = tk.Button(self.frame, text="Actualizar", command=self.goSuccess ,bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_update.grid(row=7, column=1, columnspan=2, pady=10)
        
        self.btn_back = tk.Button(self.frame, text="Volver", command=self.goBack, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_back.grid(row=8, column=1, columnspan=2, pady=10)
    
    def goSuccess(self):
        self.master.show_screen(signUpSuccess)
    
    def goBack(self):
        self.master.show_screen(signUp)
    

class AdminUpdateUser(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x450")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Actualizar Paciente" , font=("Arial", 18, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = tk.Label(self.frame, text="Nombre: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.name_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        self.cc_label = tk.Label(self.frame, text="Cédula: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.cc_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.cc_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.cc_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        self.password_label = tk.Label(self.frame, text="Contraseña: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        self.phone_label = tk.Label(self.frame, text="Teléfono: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.phone_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.phone_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        self.address_label = tk.Label(self.frame, text="Dirección: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.address_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.address_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        self.birthday_label = tk.Label(self.frame, text="Fecha de nacimiento: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.birthday_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.birthday_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.birthday_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        self.city_label = tk.Label(self.frame, text="Ciudad de residencia: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.city_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.city_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.city_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
            
        self.btn_update = tk.Button(self.frame, text="Actualizar", command=self.goSuccess ,bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_update.grid(row=7, column=1, columnspan=2, pady=10)
        
        self.btn_back = tk.Button(self.frame, text="Volver", command=self.goBack, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_back.grid(row=8, column=1, columnspan=2, pady=10)
    
    def goSuccess(self):
        self.master.show_screen(signUpSuccess)
    
    def goBack(self):
        self.master.show_screen(signUp)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)


class AdminUpdateUserSuccess(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Desea ingresar como", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        
class PatientMenu(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnReqAppointment = tk.Button(self.frame, text="Pedir Turno", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnReqAppointment.pack(pady=15)

        self.btnSearchPharmacy = tk.Button(self.frame, text="Buscar Farmacia", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnSearchPharmacy.pack(pady=15)
        
        self.btnSearchMedicine = tk.Button(self.frame, text="Buscar Medicamento", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnSearchMedicine.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        

class PatientReqAppointment(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)

class PatientAppointmentIs(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)



class PatientUpdate(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        
class PatientSearchPharmacy(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        
class PatientSearchPharmacy(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)


class PatientSearchMedicine(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        
class PharmacyMenu(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        
class PharmacyInventory(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        
        
class PharmacyUpdateMedicine(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)
        

class PharmacyUpdateMedicine(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)


class PharmacyShowInventory(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Menú pacientes", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnUpdate = tk.Button(self.frame, text="Administrador", command=self.go_to_screen, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_main_menu(self):
        self.master.show_screen(MainMenu)

class MainMenu(Screen):
    def __init__(self,master=None , list=[]):
        super().__init__(master)
        self.master = master
        self.list = list;
        self.master.geometry("700x450")
        self.pack(expand=True, fill=tk.BOTH)
        self.list = list;
        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        print(self.list)
        
        self.windowTitle = tk.Label(self.frame, text="Menú principal", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)

        self.btnSignIn = tk.Button(self.frame, text="Ingresar", command=self.go_to_sign_in, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnSignIn.pack(pady=15)

        self.btnSignUp = tk.Button(self.frame, text="Registrarse", command=self.go_to_sign_up, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnSignUp.pack(pady=15)
        
        self.btnClose = tk.Button(self.frame, text="Salir", command=self.close ,bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnClose.pack(pady=15)
    
    def go_to_sign_in(self):
        self.master.show_screen(signIn)
        
    def go_to_sign_up(self):
        self.master.show_screen(signUp)
    
    def close(self):
        self.master.destroy()
        
    

class signUp(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x350")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Registrar", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)
        
        self.btnUpdate = tk.Button(self.frame, text="Farmacia", command=self.go_to_pharmacy, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnUpdate.pack(pady=15)

        self.btnPharmacy = tk.Button(self.frame, text="Paciente",command=self.go_to_patient , bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
        
        self.btnPharmacy = tk.Button(self.frame, text="Volver",command=self.goBack,  bg="#003366", fg="white", font=("Arial", 12, "bold"), width=20)
        self.btnPharmacy.pack(pady=15)
    
    def go_to_pharmacy(self):
        self.master.show_screen(Pharmacy)
    
    def go_to_patient(self):
        self.master.show_screen(Patient)
    
    def goBack(self):
        self.master.show_screen(MainMenu)
        

class testScreen(Screen):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x570")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
        
        self.windowTitle = tk.Label(self.frame, text="Registrar", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)
        
        column_names = ["Column1", "Column2", "Column3", "Column4", "Column5"]
        
        style = ttk.Style()
        style.configure("Custom.Treeview", highlightthickness=0, bd=2, font=("Arial", 12), 
                        rowheight=30, background="#E6F2FF")
        style.configure("Custom.Treeview.Heading", font=("Arial", 13, "bold"), foreground="#003366")

        # Scrollable Frame for Table
        table_frame = tk.Frame(self.frame, bg="#E6F2FF")
        table_frame.pack(pady=(20, 0), padx=20, fill=tk.BOTH, expand=True)

        # Scrollbars
        y_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview (Table)
        self.table = ttk.Treeview(table_frame, columns=column_names, show="headings", yscrollcommand=y_scrollbar.set,
                                 style="Custom.Treeview")
        self.table.pack(fill=tk.BOTH, expand=True)
        y_scrollbar.config(command=self.table.yview)
        
        

        # Table Column Configuration
        for col in column_names:
            self.table.heading(col, text=col.title())  # Capitalize column names
            self.table.column(col, width=120, anchor="w")  # Adjust width as needed
            
        
        data = [("A1", "B1", "C1", "D1", "E1"), 
                ("A2", "B2", "C2", "D2", "E2"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A2", "B2", "C2", "D2", "E2"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A2", "B2", "C2", "D2", "E2"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
                ("A3", "B3", "C3", "D3", "E3"),
        # Add more rows as needed
        ]

        # Insert Example Data (Optional)
        if data:
            for item in data:
                self.table.insert("", tk.END, values=item)
        
        self.windowTitle = tk.Label(self.frame, text="Registrar", font=("Arial", 24, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.pack(pady=10)
    
        
    
    def go_to_pharmacy(self):
        self.master.show_screen(Pharmacy)
    
    def go_to_patient(self):
        pass
    
    def goBack(self):
        self.master.show_screen(MainMenu)

class Pharmacy(Screen):
    def __init__(self, master=None, stack = None):
        super().__init__(master)
        self.master = master
        self.stack = stack;
        self.master.geometry("700x450")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
                
        self.windowTitle = tk.Label(self.frame, text="Registrar Farmacia" , font=("Arial", 18, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = tk.Label(self.frame, text="Nombre: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        self.nit_label = tk.Label(self.frame, text="Nit: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.nit_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.nit_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.nit_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        self.password_label = tk.Label(self.frame, text="Contraseña: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.frame, show="*",font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        self.phone_label = tk.Label(self.frame, text="Teléfono: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.phone_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.phone_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        self.address_label = tk.Label(self.frame, text="Dirección: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.address_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.address_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        self.adm_label = tk.Label(self.frame, text="Administrador: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.adm_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.adm_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.adm_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        
        self.cc_adm_label = tk.Label(self.frame, text="CC Administrador: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.cc_adm_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.cc_adm_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.cc_adm_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")
            
        self.btn_update = tk.Button(self.frame, text="Registrar", command=self.savePharmacy ,bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_update.grid(row=8, column=1, columnspan=2, pady=10)
        
        self.btn_back = tk.Button(self.frame, text="Volver", command=self.goBack, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_back.grid(row=9, column=1, columnspan=2, pady=10)
        
    def cleanPharmacy(self):
        self.name_entry.delete(0, 'end')
        self.nit_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.adm_entry.delete(0, 'end')
        self.cc_adm_entry.delete(0, 'end')
 
    
    def savePharmacy(self):
        name = self.name_entry.get()
        nit = self.nit_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        admin = self.adm_entry.get()
        admin_cc = self.cc_adm_entry.get()
        
        node = NodePharmacy(name,nit,password,phone,address,admin,admin_cc)
        self.stack.push(node)
        print(self.stack.lenS())
        self.cleanPharmacy()
        self.goSuccess()
        

    def goSuccess(self):
        self.master.show_screen(signUpSuccess)
        
    def goBack(self):
        self.master.show_screen(signUp)
        
    

class Patient(Screen):
    def __init__(self, master=None, stack=None):
        super().__init__(master)
        self.master = master
        self.stack = stack
        self.master.geometry("700x450")
        self.pack(expand=True, fill=tk.BOTH)

        self.frame = tk.Frame(self, bg='#E6F2FF')
        self.frame.pack(expand=True)
                
        self.windowTitle = tk.Label(self.frame, text="Registrar Paciente" , font=("Arial", 18, "bold"), bg="#E6F2FF", fg="#003366")
        self.windowTitle.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = tk.Label(self.frame, text="Nombre: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        self.cc_label = tk.Label(self.frame, text="Cédula: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.cc_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.cc_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.cc_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        self.password_label = tk.Label(self.frame, text="Contraseña: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.frame,show="*",font=("Arial", 12))
        self.password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        self.phone_label = tk.Label(self.frame, text="Teléfono: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.phone_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.phone_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        self.address_label = tk.Label(self.frame, text="Dirección: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.address_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.address_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        self.birthday_label = tk.Label(self.frame, text="Fecha de nacimiento: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.birthday_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.birthday_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.birthday_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        
        self.city_label = tk.Label(self.frame, text="Ciudad de residencia: ", font=("Arial", 12), bg="#E6F2FF", fg="#003366")
        self.city_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.city_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.city_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")
            
        self.btn_update = tk.Button(self.frame, text="Registrar", command=self.goSuccess ,bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_update.grid(row=7, column=1, columnspan=2, pady=10)
        
        self.btn_back = tk.Button(self.frame, text="Volver", command=self.goBack, bg="#003366", fg="white", font=("Arial", 12, "bold"), width=21)
        self.btn_back.grid(row=8, column=1, columnspan=2, pady=10)
    
    def cleanPharmacy(self):
        self.name_entry.delete(0, 'end')
        self.cc_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.birthday_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')
        
 
    
    def savePharmacy(self):
        name = self.name_entry.get()
        cc = self.cc_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        birthday = self.birthday_entry.get()
        city = self.city_entry.get()
        
        node = NodePharmacy(name,cc,password,phone,address,birthday,city)
        self.stack.push(node)
        self.cleanPharmacy()
        self.goSuccess()
    
    def goSuccess(self):
        self.master.show_screen(signUpSuccess)
    
    def goBack(self):
        self.master.show_screen(signUp)
        
    


