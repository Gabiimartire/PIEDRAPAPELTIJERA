from tkinter import *
from tkinter import ttk  
import time
from scripts.reglas import mostrar_reglas
opciones = {
    'piedra':{'tijera': "Piedra aplasta a Tijeras", 'lagarto': 'Piedra aplasta a Lagarto'},
    'papel': {'piedra': "Papel cubre a Piedra", 'spock': "Papel refuta a Spock"},
    'tijera': {'papel': "Tijeras cortan a Papel", 'lagarto': "Tijeras decapitan a Lagarto"},
    'lagarto': {'papel': "Lagarto come a Papel", 'spock': "Lagarto envenena a Spock"},
    'spock': {'tijera': "Spock destroza a Tijeras", 'piedra': "Spock vaporiza a Piedra"}
}

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
        ttk.Button(self.ventana, text="Comenzar", command=self.comenzar).pack(pady=20)        # Aquí puedes agregar más elementos de la interfaz gráfica
        self.ventana.mainloop()
    def comenzar(self):
        self.label_info = ttk.Label(self.ventana, text=mostrar_reglas())     
        self.label_info.config(font=("Arial", 15), background="#1e1e1e", foreground="white")        
        self.label_info.pack(pady=20)
        self.label_info.place(relx=0.5, rely=0.5, anchor=CENTER)
        ttk.Button(self.ventana, text="Siguiente", command=self.limpiar_pantalla).pack(pady=10)
    def limpiar_pantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
        self.jugar()
    def jugar(self):
        self.ventana.update()
        info1 = ttk.Label(self.ventana, text="A la cuenta de tres, elige escribe tu opción:")
        info1.config(font=("Arial", 25), background="#1e1e1e", foreground="white")
        info1.pack(pady=20)
        info1.place(relx=0.5, rely=0.3, anchor=CENTER)
        info2 = ttk.Label(self.ventana, text="")
        info2.config(font=("Arial", 35), background="#1e1e1e", foreground="white")
        info2.place(relx=0.5, rely=0.2, anchor=CENTER)
        info2.pack(pady=20)
        for i in range(3, 0, -1):
            info2.config(text=str(i))
            self.ventana.update()
            time.sleep(1)
        ingrese_opcion = ttk.Entry(self.ventana)
        ingrese_opcion.pack(pady=20)
        ingrese_opcion.config(font=("Arial", 20), width=20)
        ingrese_opcion.place(relx=0.5, rely=0.7, anchor=CENTER)
        ingrese_opcion.focus()

def main():
    app = MainInterfaz()
    return 0

if __name__ == "__main__":
    main()