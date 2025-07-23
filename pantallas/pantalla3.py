from tkinter import *
from tkinter import ttk
import time
from scripts.matcheo import matcheo
from pantallas.clean import limpiar_pantalla
import random
opciones = {
    'piedra':{'tijera': "Piedra aplasta a Tijeras", 'lagarto': 'Piedra aplasta a Lagarto'},
    'papel': {'piedra': "Papel cubre a Piedra", 'spock': "Papel refuta a Spock"},
    'tijera': {'papel': "Tijeras cortan a Papel", 'lagarto': "Tijeras decapitan a Lagarto"},
    'lagarto': {'papel': "Lagarto come a Papel", 'spock': "Lagarto envenena a Spock"},
    'spock': {'tijera': "Spock destroza a Tijeras", 'piedra': "Spock vaporiza a Piedra"}
}

def jugar(app):
        limpiar_pantalla(app)
        contenedor = Frame(app.ventana, bg="#1e1e1e")
        contenedor.pack(fill=BOTH, expand=True)
        app.ventana.update()
        info1 = ttk.Label(contenedor, text="A la cuenta de tres, elige escribe tu opción:")
        info1.config(font=("Arial", 25), background="#1e1e1e", foreground="white")
        info1.pack(pady=20)
        info1.place(relx=0.5, rely=0.3, anchor=CENTER)
        info2 = ttk.Label(contenedor, text="")
        info2.config(font=("Arial", 35), background="#1e1e1e", foreground="white")
        info2.place(relx=0.5, rely=0.2, anchor=CENTER)
        info2.pack(pady=10)
        for i in range(3, 0, -1):
            info2.config(text=str(i))
            app.ventana.update()
            time.sleep(1)
        ingrese_opcion = ttk.Entry(contenedor)
        ingrese_opcion.pack(pady=20)
        ingrese_opcion.config(font=("Arial", 20), width=20)
        ingrese_opcion.place(relx=0.5, rely=0.7, anchor=CENTER)
        ingrese_opcion.focus()
        ttk.Button(contenedor, text="Enviar", command=lambda: procesar_opcion(app, ingrese_opcion.get(), contenedor)).pack(pady=20)
        
def procesar_opcion(app, opcion_usuario, contenedor):
    if not opcion_usuario.lower().strip() in opciones:
        return 0
    opciones_usuario = opcion_usuario.lower().strip()
    if opciones_usuario not in opciones:
        app.label_info = ttk.Label(contenedor, text="Opción no válida. Por favor, elige entre piedra, papel, tijera, lagarto o spock.")
        app.label_info.config(font=("Arial", 15), background="#1e1e1e", foreground="white")
        app.label_info.pack(pady=20)
    else:
        cpu_opcion = random.choice(list(opciones.keys()))
        app.label_info = ttk.Label(contenedor, text=f"Elegiste: {opcion_usuario.capitalize()}\nLa CPU elegirá su opción...")
        app.label_info.config(font=("Arial", 15), background="#1e1e1e", foreground="white")            
        app.label_info.pack(pady=20)
        app.label_info.place(relx=0.5, rely=0.5, anchor=CENTER)
        contenedor.update()
        time.sleep(2)
        contenedor.update()
        app.label_info.config(text=f"La CPU eligió: {cpu_opcion.capitalize()}")
        app.label_info.pack(pady=20)
        app.label_info.place(relx=0.5, rely=0.5, anchor=CENTER)
        time.sleep(1)
        app.label_info.config(text="")
        app.label_info.config(text=matcheo(opciones_usuario, cpu_opcion, opciones, "Gabriel"))
        app.label_info.pack(pady=50)
        app.label_info.place(relx=0.5, rely=0.9, anchor=CENTER)
        ttk.Button(contenedor, text="Reiniciar", command=lambda: jugar(app)).pack(pady=50)

