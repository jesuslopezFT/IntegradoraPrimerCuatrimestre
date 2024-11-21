import ControlarInventario as ctrl

import tkinter as tk
from functools import partial

# Funciones generales
def AgregarOReducir(menuPrincipal, valor):
    if (not ctrl.ChecarSiSeHaSeleccionadoProducto()):
        return
    ctrl.inventario[ctrl.productoSeleccionado][1] += valor
    ctrl.ActualizarInventario(menuPrincipal)

def Agregar1(menuPrincipal): AgregarOReducir(menuPrincipal, +1)
def Reducir1(menuPrincipal): AgregarOReducir(menuPrincipal, -1)

# Funciones especializadas
def IniciarMenu(menuPrincipal):
    Agregar = tk.Button(menuPrincipal, 
        text= " + 1 ",
        width= 15, height= 1,
        command= partial(Agregar1, menuPrincipal))
    Agregar.grid(row= 4, column= 175)

    Reducir = tk.Button(menuPrincipal,
        text= " - 1",
        width= 15, height= 1,
        command= partial(Reducir1, menuPrincipal))
    Reducir.grid(row= 5, column= 175)