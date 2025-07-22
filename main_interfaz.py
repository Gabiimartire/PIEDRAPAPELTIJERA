from tkinter import *
from tkinter import ttk  

from scripts.reglas import mostrar_reglas
class MainInterfaz:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Piedra, papel, tijera, lagarto o spock")
        self.ventana.geometry("1024x768")
        self.ventana.configure(bg="#1e1e1e")
        self.ventana.resizable(True, True)
        self.label_info = ttk.Label(self.ventana, text="¡Bienvenido al juego de Piedra, Papel, Tijera, Lagarto o Spock!")
        self.label_info.config(font=("Arial", 20), background="#1e1e1e", foreground="white")
        self.label_info.pack(pady=20)
        ttk.Button(self.ventana, text="Comenzar", command=self.comenzar).pack(pady=20)
        ttk.Button(self.ventana, text="Siguiente", command=self.limpiar_pantalla).pack(pady=10)
        # Aquí puedes agregar más elementos de la interfaz gráfica
        self.ventana.mainloop()
    def comenzar(self):
        self.label_info = ttk.Label(self.ventana, text=mostrar_reglas())     
        self.label_info.config(font=("Arial", 15), background="#1e1e1e", foreground="white")        
        self.label_info.pack(pady=20)
        self.label_info.place(relx=0.5, rely=0.5, anchor=CENTER)
    def limpiar_pantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
        

def main():
    app = MainInterfaz()
    return 0

if __name__ == "__main__":
    main()