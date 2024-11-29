from ControlarInventario import *

import tkinter as tk
from tkinter import messagebox
from functools import partial

def AgregarCantidad(menuPrincipal):
    if (not ChecarSiSeHaSeleccionadoProducto()):
        return
    
    if (entradaCantidad.get() == ""):
        messagebox.showwarning("Aviso", "Entrada vacia")
        return
    
    try:
        valor = int(entradaCantidad.get())
    except:
        messagebox.showerror("Error", "Valor introducido invalido")
        return

    inventario[productoSeleccionado["Indice"]].unidades += valor
    ActualizarProducto(menuPrincipal,
                       productoSeleccionado["Indice"],
                       2 + (productoSeleccionado["Indice"] // 5),
                       25 + ( (25 * productoSeleccionado["Indice"]) - ((productoSeleccionado["Indice"] // 5) * 125 )))
    AgregarEtiquetaCantidad(menuPrincipal, inventario[productoSeleccionado["Indice"]].unidades, inventario[productoSeleccionado["Indice"]].ventas)

def IniciarMenu(menuPrincipal):
    global entradaCantidad
    entradaCantidad = tk.Entry(menuPrincipal,
        width=20)
    entradaCantidad.grid(row= 9, column= 175)

    cantidad = tk.Button(menuPrincipal,
            text= "Agregar Unidades:",
            width= 15, height= 1,
            command= partial(AgregarCantidad, menuPrincipal))
    cantidad.grid(row= 8, column= 175)