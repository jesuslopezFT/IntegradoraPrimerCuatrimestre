import ControlarInventario as ctrl
import AgregarProducto as agg

import tkinter as tk

# Valores

# Funciones

# Tkinter
menuPrincipal = tk.Tk()
menuPrincipal.title("Control de Inventario")

Titulo = tk.Label(menuPrincipal,
    text= "Control de Inventario",
    width= 25, height=2)
Titulo.grid(row= 1, column= 25)

agg.IniciarMenu(menuPrincipal)

ctrl.IniciarMenu(menuPrincipal)

menuPrincipal.mainloop()
