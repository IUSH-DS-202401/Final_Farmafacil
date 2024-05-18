import tkinter as tk
from screens import Pharmacy
from modules.stack import Stack

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Farma Facil")
        stackPharmacy = Stack()
        self.current_screen = Pharmacy(self, stackPharmacy)
        self.current_screen.pack()
    
    def show_screen(self, screen_class):
        new_screen = screen_class(self)
        if self.current_screen is not None:
            self.current_screen.destroy()
        self.current_screen = new_screen
        self.current_screen.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()