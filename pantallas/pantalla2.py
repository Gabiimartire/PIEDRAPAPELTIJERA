from tkinter import *
from tkinter import ttk  
from scripts.reglas import mostrar_reglas
from pantallas.pantalla3 import jugar
def comenzar(app):
        app.label_info = ttk.Label(app.ventana, text=mostrar_reglas())     
        app.label_info.config(font=("Arial", 15), background="#1e1e1e", foreground="white")        
        app.label_info.pack(pady=20)
        app.label_info.place(relx=0.5, rely=0.5, anchor=CENTER)
        ttk.Button(app.ventana, text="Siguiente", command=lambda: jugar(app)).pack(pady=10)
        