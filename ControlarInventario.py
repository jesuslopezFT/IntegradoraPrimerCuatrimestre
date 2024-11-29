import tkinter as tk
from tkinter import messagebox  
from functools import partial

# Clases
class Producto:
    def __init__(self, nombre : str, unidades : int, ventas : int):
        self.nombre = nombre
        self.unidades = unidades
        self.ventas = ventas
# Valores
inventario = []
"""
Lista de productos, estos tienen propiedades: nombre, unidades y ventas.
<b>Utilice productoSeleccionado["Indice"] como indice en el inventario para utilizar el producto seleccionado</b>
"""

# 2024 Nov 20: Este es para pruebas 
inventario = [ Producto("Papitas", 2, 0), Producto("Sodas", 2, 1), Producto("Dulces", 1, 10), Producto("Chocolates", 4, 0), Producto("Aguas", 10, 25), Producto("Cacahuates", 1, 5) ]

#inventario = []
seHaSeleccionadoAlgo = False
productoSeleccionado = {"Indice": -1, "Fila": 2, "Columna": 25}
"""
Contiene el indice, la fila y la columna; pero no es el producto en si. El indice es en que posicion del inventario esta el producto seleccionado
"""
global listaProductos
"""
Guarda la cantidad de productos, utilizado principalmente a la hora de borrar productos 
"""


# Funciones genericas
def ActualizarInventario(menuPrincipal):
    """
    Actualiza todo el inventario, en caso de solamente querer actualizar un producto, por favor use ActualizarProducto
    """

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
        boton = tk.Button(menuPrincipal, text= f"\"{inventario[indice].nombre}\": \n" +
                f"{inventario[indice].unidades} Unidades; {inventario[indice].ventas} Ventas", 
            width= 25, height= 2,
            command= partial(SeleccionarProducto, menuPrincipal, indice, fila, columna) )
        boton.grid(row= fila, column= columna)

def AgregarEtiquetaNombre(menuPrincipal, nombre = ""):
    """
    Cambia el nombre del producto seleccionado, unicamente poner el nombre del producto.
    La parte estetica del producto ya esta integrara en esta funcion
    """
    Nombre = tk.Label(menuPrincipal,
        text= f"Producto Seleccionado: \n \"{nombre}\"",
        width= 25, height= 2)
    Nombre.grid(row= 2, column= 175)

def AgregarEtiquetaCantidad(menuPrincipal, unidades = 0, ventas = 0):
    """
    Cambia las unidades y ventas del producto seleccionado, unicamente poner valor de unidades y ventas.
    La parte estetica del texto ya esta integrada en esta funcion
    """
    Cantidad = tk.Label(menuPrincipal,
        text= f"Unidades / Ventas: \n {unidades} / {ventas}",
        width=25, height= 2)
    Cantidad.grid(row= 3, column= 175)

def ChecarSiSeHaSeleccionadoProducto():
    """
    Esta funcion checa si se ha seleccionado un producto:
    En caso de que no manda un aviso al usuario y devuelve false.
    En caso de que si devuelve true
    """
    if (not seHaSeleccionadoAlgo or len(inventario) <= 0): 
        messagebox.showwarning("Aviso", "No se ha seleccionado un producto")
        return False
    else: return True


# Funciones especializadas 
def IniciarMenu(menuPrincipal):
    ActualizarInventario(menuPrincipal)
    AgregarEtiquetaNombre(menuPrincipal)
    AgregarEtiquetaCantidad(menuPrincipal)


def SeleccionarProducto(menuPrincipal,
        indice, fila, columna):
    global seHaSeleccionadoAlgo
    global productoSeleccionado

    seHaSeleccionadoAlgo = True
    productoSeleccionado["Indice"] = indice
    productoSeleccionado["Fila"] = fila
    productoSeleccionado["Columna"] = columna

    AgregarEtiquetaNombre(menuPrincipal, inventario[indice].nombre)
    AgregarEtiquetaCantidad(menuPrincipal, inventario[indice].unidades, inventario[indice].ventas)