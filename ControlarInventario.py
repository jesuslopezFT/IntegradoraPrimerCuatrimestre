import tkinter as tk
from tkinter import messagebox,ttk  
from functools import partial

# 2024 Nov 20: Este era para pruebas 
#inventario = [ ["Papitas", 2], ["Sodas", 3], ["Dulces", 1], ["Chocolates", 4], ["Aguas", 10], ["Cacahuates", 1] ]

# Valores
inventario = []
seHaSeleccionadoAlgo = False
productoSeleccionado = -1

# Funciones genericas
def ActualizarInventario(menuPrincipal):
    for i in range(len(inventario)):
        boton = tk.Button(menuPrincipal, text= f"\"{inventario[i][0]}\": \n{inventario[i][1]}", 
                        width= 25, height= 2,
                        command= partial(SeleccionarProducto, i, menuPrincipal))
        boton.grid(row= 2 + (i // 5), column= 25 + ( (25 * i) - ((i // 5) * 125 )) )

def AgregarEtiquetaNombre(menuPrincipal, texto):
    Nombre = tk.Label(menuPrincipal,
        text= texto,
        width= 25, height= 2)
    Nombre.grid(row= 2, column= 175)

def AgregarEtiquetaCantidad(menuPrincipal, texto):
    Cantidad = tk.Label(menuPrincipal,
        text= texto,
        width=25, height= 2)
    Cantidad.grid(row= 3, column= 175)

def ChecarSiSeHaSeleccionadoProducto():
    if (not seHaSeleccionadoAlgo or len(inventario) <= 0): 
        messagebox.showwarning("Aviso", "No se ha seleccionado un producto")
        return False

# Funciones especializadas 
def IniciarMenu(menuPrincipal):
    AgregarEtiquetaNombre(menuPrincipal, "Producto Seleccionado: ")
    AgregarEtiquetaCantidad(menuPrincipal, "Cantidad: ")


def SeleccionarProducto(indice,
        menuPrincipal):
    
    global seHaSeleccionadoAlgo

    seHaSeleccionadoAlgo = True
    productoSeleccionado = indice

    AgregarEtiquetaNombre(menuPrincipal, f"Producto Seleccionado: \n \"{inventario[productoSeleccionado][0]}\"")
    AgregarEtiquetaCantidad(menuPrincipal, f"Cantidad: \n \"{inventario[productoSeleccionado][1]}\"")