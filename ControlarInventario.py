import tkinter as tk
from functools import partial

# 2024 Nov 20: Este era para pruebas 
#inventario = [ ["Papitas", 2], ["Sodas", 3], ["Dulces", 1], ["Chocolates", 4], ["Aguas", 10], ["Cacahuates", 1] ]

# Valores
inventario = []

# Funciones
def ActualizarInventario(menuPrincipal):
    for i in range(len(inventario)):
        boton = tk.Button(menuPrincipal, text= f"\"{inventario[i][0]}\": \n{inventario[i][1]}", 
                        width= 25, height= 2,
                        command= partial(SeleccionarProducto, inventario[i][0], menuPrincipal))
        boton.grid(row= 2 + (i // 5), column= 25 + ( (25 * i) - ((i // 5) * 125 )) )

def IniciarMenu(menuPrincipal):
    Seleccionado = tk.Label(menuPrincipal,
        text= "Producto Seleccionado:",
        width= 25, height= 2)
    Seleccionado.grid(row= 2, column= 175)

def SeleccionarProducto(Nombre,
        menuPrincipal):

    Seleccionado = tk.Label(menuPrincipal ,
        text=f"Producto Seleccionado: \n \"{Nombre}\"", 
        width= 25, height= 2)
    Seleccionado.grid(row= 2, column= 175)