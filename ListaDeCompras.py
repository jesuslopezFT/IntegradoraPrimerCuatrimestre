import ControlarInventario as ctrl
import Vender as vend

import tkinter as tk
from tkinter import messagebox
from functools import partial

# Valores
listaCompras = {}
"""
Diccionario de los productos que se planean comprar, sus llaves son los nombres de los productos. Sus valores son listas de dos elementos: Nombre del producto y unidades a vender
"""

# Funciones
def ActualizarLista(menuPrincipal):
    global listaTitulo

    if (len(listaCompras) <= 0):
        listaTitulo = tk.Label(menuPrincipal, text= "", width= 25)
        listaTitulo.grid(row= 8, column= 1)
    else:
        textoLista = ""
        for nombre, unidades in listaCompras.values():
            textoLista += f"\"{nombre}\": {unidades} \n"

        listaTitulo = tk.Label(menuPrincipal, text= f"Lista de compras: \n{textoLista}", width= 25)
        listaTitulo.grid(row= 8, column= 1)

def Enlistar1(menuPrincipal): Enlistar(menuPrincipal, 1)
def EnlistarTodo(menuPrincipal): Enlistar(menuPrincipal, ctrl.inventario[ctrl.productoSeleccionado["Indice"]].unidades)
def Enlistar(menuPrincipal : tk.Tk ,valor : int = 0, usarEntrada : bool = False):
    global enlistarEntrada

    if (not ctrl.ChecarSiSeHaSeleccionadoProducto()):
        return

    producto = ctrl.inventario[ctrl.productoSeleccionado["Indice"]]

    try:
        if (valor + listaCompras[producto.nombre][1]) > producto.unidades:
            messagebox.showwarning("Aviso", "Se intento enlistar una cantidad mayor de la que hay disponible. Se tomo el valor de las unidades, en caso de querer agregar mas, por favor, agregue mas unidades en existencia al producto.")
            listaCompras[producto.nombre][1] = producto.unidades
            ActualizarLista(menuPrincipal)
            return
    except:
        pass

    if not usarEntrada:
        try:
            listaCompras[producto.nombre] = [producto.nombre, valor + listaCompras[producto.nombre][1]]
        except:
            listaCompras[producto.nombre] = [producto.nombre, valor]
    else:
        valorEtiqueta = 0

        if (enlistarEntrada.get == None or enlistarEntrada.get == ""):
            messagebox.showwarning("Aviso", "Entrada vacia.")
            return
        try:
            valorEtiqueta = int(enlistarEntrada.get())
        except:
            messagebox.showerror("Error", "Valor introducido invalido")
            return


        try:
            listaCompras[producto.nombre] = [producto.nombre, valor + valorEtiqueta]
        except:
            listaCompras[producto.nombre] = [producto.nombre, valorEtiqueta]

    ActualizarLista(menuPrincipal)

def Vender(menuPrincipal):
    """
    Este metodo no es para vender un producto, es para vender toda en la lista de compras. El metodo para vender un producto esta en el archivo Vender.py
    """
    
    global listaCompras

    if (len(listaCompras) <= 0):
        messagebox.showwarning("Aviso", "La lista de compras esta vacia")
        return
    
    for nombres, unidades in listaCompras.values():
        for j in range(len(ctrl.inventario)):
            if (nombres == ctrl.inventario[j].nombre):
                ctrl.inventario[j].unidades -= unidades
                ctrl.inventario[j].ventas += unidades
    
                
    listaTitulo.config(text= " \n \n \n")
    listaCompras.clear()
    ActualizarLista(menuPrincipal)

    ctrl.ActualizarInventario(menuPrincipal)

# Cosas de tkinter
def IniciarMenu(menuPrincipal):
    enlistar1 = tk.Button(menuPrincipal, 
        text="Enlistar 1", 
        width= 15,
        command= partial(Enlistar1, menuPrincipal))
    enlistar1.grid(row= 10, column= 175)

    enlistarTodo = tk.Button(menuPrincipal,
        text="Enlistar Todo",
        width= 15,
        command= partial(EnlistarTodo, menuPrincipal))
    enlistarTodo.grid(row=11, column= 175)

    global enlistarEntrada
    enlistarEntrada = tk.Entry(menuPrincipal,
        width= 20)
    enlistarEntrada.grid(row=13, column= 175)
    enlistarX = tk.Button(menuPrincipal,
        text= "Enlistar unidades:",
        width= 15,
        command= partial(Enlistar, menuPrincipal, usarEntrada = True))
    enlistarX.grid(row=12, column= 175)

    venderLista = tk.Button(menuPrincipal,
        text= "Vender lista",
        width= 15, height= 2,
        command= partial(Vender, menuPrincipal))
    venderLista.grid(row= 7, column= 1)

    ActualizarLista(menuPrincipal)