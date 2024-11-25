import ControlarInventario as ctrl
import AgregarProducto as agg
import Vender as vender
import AgregarCantidad as cant
import EliminarProducto as elim

import tkinter as tk

menuPrincipal = tk.Tk()
menuPrincipal.title("Control de Inventario")

Titulo = tk.Label(menuPrincipal,
    text= "Control de Inventario",
    width= 25, height=2)
Titulo.grid(row= 1, column= 25)

agg.IniciarMenu(menuPrincipal)

ctrl.IniciarMenu(menuPrincipal)

vender.IniciarMenu(menuPrincipal)

cant.IniciarMenu(menuPrincipal)

elim.IniciarMenu(menuPrincipal)

menuPrincipal.mainloop()