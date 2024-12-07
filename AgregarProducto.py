from ControlarInventario import *

import tkinter as tk
from functools import partial

def AgregarProducto(menuPrincipal, 
    Nombre : tk.Entry, 
    Cantidad : tk.Entry):
        
    if (not Nombre.get() or Nombre.get() == ""):
        messagebox.showerror("Error", "Texto vacio")
        return
    elif (ChecarOtrosProductosAntes(Nombre)):
        messagebox.showinfo("Aviso", "Producto ya existe")
        return 

    if (not Cantidad.get() or Cantidad.get() == ""):
        messagebox.showerror("Error" , "Cantidad vacia")
        return

    valor = 0

    try:
        valor = int(Cantidad.get())
    except:
        messagebox.showerror("Error", "Valor invalido, debe ser un numero entero")
        return


    inventario.append(Producto(Nombre.get(), valor, 0))
    nombres_productos.append(Nombre.get())
    ventas_productos.append(0)

    ActualizarInventario(menuPrincipal)

def IniciarMenu(menuPrincipal):
        
        NombreTitulo = tk.Label(menuPrincipal,
            text= "Nombre del Producto:",
            width= 25, height= 1)
        NombreTitulo.grid(row= 3, column= 1)
        Nombre = tk.Entry(menuPrincipal,
            width= 15)
        Nombre.grid(row=4, column= 1)
    
        CantidadTitulo = tk.Label(menuPrincipal,
            text= "Cantidad del Producto:",
            width= 25, height= 1)
        CantidadTitulo.grid(row= 5, column= 1)
        Cantidad = tk.Entry(menuPrincipal,
            width= 15)
        Cantidad.grid(row= 6, column= 1)

        BotonAgregar = tk.Button(menuPrincipal,
            text= "Agregar Producto", 
            width= 15, height= 2,
            command= partial(AgregarProducto, menuPrincipal, Nombre, Cantidad))
        BotonAgregar.grid(row= 2, column= 1)

def ChecarOtrosProductosAntes(Nombre : tk.Entry):
    for i in range(len(inventario)):
        if (Nombre.get() == inventario[i].nombre): return True
    return False   