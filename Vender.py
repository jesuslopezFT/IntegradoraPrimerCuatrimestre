import ControlarInventario as ctrl

import tkinter as tk
from tkinter import messagebox, ttk
from functools import partial

# Funciones generales
def Vender(menuPrincipal, valor, usarEntrada = False):
    if (not ctrl.ChecarSiSeHaSeleccionadoProducto()):
        return
    
    if (ctrl.inventario[ctrl.productoSeleccionado["Indice"]].unidades <= 0):
        messagebox.showwarning("Aviso", "Este producto se ha agotado")
        return
    
    if (not usarEntrada):
        ctrl.inventario[ctrl.productoSeleccionado["Indice"]].unidades -= valor
        ctrl.inventario[ctrl.productoSeleccionado["Indice"]].ventas += valor
    else:
        if (not EntradaVenderX.get() or EntradaVenderX.get() == ""):
            messagebox.showwarning("Aviso", "Cantidad para vender vacia")
            return
        try:
            nuevoValor = int(EntradaVenderX.get())
            ctrl.inventario[ctrl.productoSeleccionado["Indice"]].unidades -= nuevoValor
            ctrl.inventario[ctrl.productoSeleccionado["Indice"]].ventas += nuevoValor
        except:
            messagebox.showerror("Error", "Valor introducido invalido")
            return

    ctrl.AgregarEtiquetaCantidad(menuPrincipal, f"Unidades / Ventas: \n{ctrl.inventario[ctrl.productoSeleccionado["Indice"]].unidades} / {ctrl.inventario[ctrl.productoSeleccionado["Indice"]].ventas}")
    
    indice = ctrl.productoSeleccionado["Indice"]
    fila = 2 + (indice // 5)
    columna = 25 + ( (25 * indice) - ((indice // 5) * 125 ))

    ctrl.ActualizarProducto(menuPrincipal, indice, fila, columna)

def Vender1(menuPrincipal): Vender(menuPrincipal, 1)
def VenderTodo(menuPrincipal): 
    if (not ctrl.ChecarSiSeHaSeleccionadoProducto()):
        return
    Vender(menuPrincipal, ctrl.inventario[ctrl.productoSeleccionado["Indice"]].unidades)

# Funciones especializadas
def IniciarMenu(menuPrincipal):
    BotonVender1 = tk.Button(menuPrincipal,
        text= " Vender 1",
        width= 15, height= 1,
        command= partial(Vender1, menuPrincipal))
    BotonVender1.grid(row= 4, column= 175)

    BotonVenderTodo = tk.Button(menuPrincipal,
        text= "Vender Todo",
        width= 15, height= 1,
        command= partial(VenderTodo, menuPrincipal))
    BotonVenderTodo.grid(row= 5, column= 175)

    global EntradaVenderX 
    EntradaVenderX = tk.Entry(menuPrincipal,
        width= 20)
    EntradaVenderX.grid(row= 7, column= 175)
    BotonVenderX = tk.Button(menuPrincipal,
        text= "Vender: ",
        width= 15, height= 1,
        command= partial(Vender, menuPrincipal, 0, True))
    BotonVenderX.grid(row= 6, column= 175)
    