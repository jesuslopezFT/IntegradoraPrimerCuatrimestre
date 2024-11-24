import ControlarInventario as ctrl

import tkinter as tk
from tkinter import messagebox
from functools import partial

def EliminarProducto(menuPrincipal):
    if (not ctrl.ChecarSiSeHaSeleccionadoProducto()):
        return
    
    ctrl.inventario.pop(ctrl.productoSeleccionado["Indice"])
    ctrl.productoSeleccionado["Indice"] = -1
    ctrl.IniciarMenu(menuPrincipal)
    ctrl.ActualizarInventario(menuPrincipal)

def IniciarMenu(menuPrincipal):
    eliminar = tk.Button(menuPrincipal,
        text= "Eliminar Producto",
        width= 15, height= 1,
        command= partial(EliminarProducto, menuPrincipal))
    eliminar.grid(row= 10, column= 175)