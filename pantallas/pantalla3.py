from tkinter import *
from tkinter import ttk
import time
from scripts.matcheo import matcheo
from pantallas.clean import limpiar_pantalla
import random
from PIL import Image, ImageTk
opciones = {
    'piedra':{'tijera': "Piedra aplasta a Tijeras", 'lagarto': 'Piedra aplasta a Lagarto'},
    'papel': {'piedra': "Papel cubre a Piedra", 'spock': "Papel refuta a Spock"},
    'tijera': {'papel': "Tijeras cortan a Papel", 'lagarto': "Tijeras decapitan a Lagarto"},
    'lagarto': {'papel': "Lagarto come a Papel", 'spock': "Lagarto envenena a Spock"},
    'spock': {'tijera': "Spock destroza a Tijeras", 'piedra': "Spock vaporiza a Piedra"}
}

def jugar(app):
    limpiar_pantalla(app)

    frame = Frame(app.ventana, bg="#1e1e1e")
    frame.pack(expand=True)
    
    # Mensaje de cuenta regresiva
    info1 = ttk.Label(frame, text="A la cuenta de tres, escribe tu opción:")
    info1.config(font=("Arial", 20), background="#1e1e1e", foreground="white")
    info1.grid(row=0, column=0, columnspan=2, pady=20)

    info2 = ttk.Label(frame, text="")
    info2.config(font=("Arial", 30), background="#1e1e1e", foreground="white")
    info2.grid(row=1, column=0, columnspan=2, pady=10)

    app.ventana.update()
    for i in range(3, 0, -1):
        info2.config(text=str(i))
        app.ventana.update()
        time.sleep(1)

    # Entrada de opción
    #ingrese_opcion = ttk.Entry(frame, font=("Arial", 20), width=25)
    #ingrese_opcion.grid(row=2, column=0, columnspan=2, pady=20)
    #ingrese_opcion.focus()
    frame_iconos = Frame(app.ventana, bg="#1e1e1e")
    frame_iconos.pack(pady=20)
    opciones_2 = ["piedra", "papel", "tijeras", "lagarto", "spock"]

    for opcion in opciones_2:
        img = Image.open(f"./pantallas/images/{opcion}.png").resize((100, 100), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        lbl = ttk.Label(frame_iconos, image=img_tk, background="#1e1e1e")
        lbl.image = img_tk
        lbl.pack(side=LEFT, padx=10)
        lbl.bind("<Button-1>", lambda e, opcion=opcion: procesar_opcion(app, opcion, frame))
    # Distribuir columnas dentro del frame
    for i in range(len(opciones_2)):
        frame.grid_columnconfigure(i, weight=1)

    
    # Botón enviar
    #boton_enviar = ttk.Button(frame, text="Enviar", command=lambda: procesar_opcion(app, ingrese_opcion.get(), frame))
    #boton_enviar.grid(row=3, column=0, columnspan=2, pady=10)

    # Guardar el frame por si querés destruirlo después
    app.frame_actual = frame

def procesar_opcion(app, opcion_usuario, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    opciones_usuario = opcion_usuario.lower().strip()
    if opciones_usuario not in opciones:
        mensaje = "Opción no válida. Por favor, elige entre piedra, papel, tijera, lagarto o spock."
    else:
        cpu_opcion = random.choice(list(opciones.keys()))
        resultado = matcheo(opciones_usuario, cpu_opcion, opciones, "Gabriel")
        mensaje = f"Elegiste: {opcion_usuario.capitalize()}\nLa CPU eligió: {cpu_opcion.capitalize()}\n\n{resultado}"

    label_resultado = ttk.Label(frame, text=mensaje)
    label_resultado.config(font=("Arial", 15), background="#1e1e1e", foreground="white")
    label_resultado.grid(row=0, column=0, columnspan=2, pady=20)

    boton_reiniciar = ttk.Button(frame, text="Reiniciar", command=lambda: jugar(app))
    boton_reiniciar.grid(row=1, column=0, columnspan=2, pady=10)
    boton_salir = ttk.Button(frame, text="Salir", command=app.ventana.quit)
    boton_salir.grid(row=2, column=0, columnspan=2, pady=10)
