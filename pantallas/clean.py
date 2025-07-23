from tkinter import *
def limpiar_pantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
