import tkinter as tk

#Valores
inventario = {}

# Tkinter
menuPrincipal = tk.Tk()
menuPrincipal.title("Control de Inventario")

Titulo = tk.Label(menuPrincipal, text= "Control de Inventario", width= 25)
Titulo.grid(row= 1, column= 1)

BotonAgregar = tk.Button(menuPrincipal, text= "Agregar Producto", width= 15)
BotonAgregar.grid(row= 2, column= 1)

menuPrincipal.mainloop()