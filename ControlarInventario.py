import tkinter as tk
from tkinter import messagebox  
from functools import partial

# Clases
class Producto:
    def __init__(self, nombre : str, unidades : int, ventas : int):
        self.nombre = nombre
        self.unidades = unidades
        self.ventas = ventas

# 2024 Nov 20: Este es para pruebas 
inventario = [ Producto("Papitas", 2, 0), Producto("Sodas", 2, 1), Producto("Dulces", 1, 10), Producto("Chocolates", 4, 0), Producto("Aguas", 10, 25), Producto("Cacahuates", 1, 5) ]

# Valores
#inventario = []
seHaSeleccionadoAlgo = False
productoSeleccionado = {"Indice": -1, "Fila": 2, "Columna": 25}
global listaProductos


# Funciones genericas
def ActualizarInventario(menuPrincipal):
    global listaProductos

    try:
        if (len(inventario) >= listaProductos): listaProductos = len(inventario)
    except:
        listaProductos = len(inventario)

    for i in range(listaProductos):

        fila = 2 + (i // 5)
        columna = 25 + ( (25 * i) - ((i // 5) * 125 ))

        ActualizarProducto(menuPrincipal, 
        i, fila, columna)
def ActualizarProducto(menuPrincipal,
        indice, fila, columna):

    if (indice >= len(inventario)):
        boton = tk.Button(menuPrincipal, width= 25, height= 2)
        boton.grid(row = fila, column= columna)
        return
    else:  
        boton = tk.Button(menuPrincipal, width= 25, height= 2)

        boton = tk.Button(menuPrincipal, text= f"\"{inventario[indice].nombre}\": \n" +
                f"{inventario[indice].unidades} Unidades; {inventario[indice].ventas} Ventas", 
            width= 25, height= 2,
            command= partial(SeleccionarProducto, menuPrincipal, indice, fila, columna) )
        boton.grid(row= fila, column= columna)


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
    else: return True

# Funciones especializadas 
def IniciarMenu(menuPrincipal):
    ActualizarInventario(menuPrincipal)
    AgregarEtiquetaNombre(menuPrincipal, "Producto Seleccionado: ")
    AgregarEtiquetaCantidad(menuPrincipal, "Unidades / Ventas: ")


def SeleccionarProducto(menuPrincipal,
        indice, fila, columna):
    
    global seHaSeleccionadoAlgo
    global productoSeleccionado

    seHaSeleccionadoAlgo = True
    productoSeleccionado["Indice"] = indice
    productoSeleccionado["Fila"] = fila
    productoSeleccionado["Columna"] = columna

    AgregarEtiquetaNombre(menuPrincipal, f"Producto Seleccionado: \n \"{inventario[indice].nombre}\"")
    AgregarEtiquetaCantidad(menuPrincipal, f"Unidades / Ventas: \n {inventario[indice].unidades} / {inventario[indice].ventas}")