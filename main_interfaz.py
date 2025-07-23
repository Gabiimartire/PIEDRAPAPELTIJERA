from tkinter import *
from tkinter import ttk  
from pantallas.pantalla2 import comenzar

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
        self.label_info2 = ttk.Label(self.ventana, text="Presione Comenzar para ver las reglas del juego")
        self.label_info2.config(font=("Arial", 15), background="#1e1e1e", foreground="white")
        self.label_info2.pack(pady=20)
        ttk.Button(self.ventana, text="Comenzar", command=lambda: comenzar(self)).pack(pady=20)        # Aquí puedes agregar más elementos de la interfaz gráfica
        self.ventana.mainloop()

def main():
    app = MainInterfaz()
    return 0

if __name__ == "__main__":
    main()