from ControlarInventario import *

import tkinter as tk
from functools import partial

def AgregarProducto(menuPrincipal, 
    Nombre : tk.Entry, NombreEstado : tk.Label, 
    Cantidad : tk.Entry, CantidadEstado : tk.Label):
        
        if (not Nombre.get() or Nombre.get() == ""):
            NombreEstado.config(text="Texto Vacio")
            return
        elif (ChecarOtrosProductosAntes(Nombre)):
            NombreEstado.config(text="Ya existe")
            return 
        else: NombreEstado.config(text="")

        if (not Cantidad.get() or Cantidad.get() == ""):
            CantidadEstado.config(text= "Cantidad Vacia")
            return

        valor = 0

        try:
            valor = int(Cantidad.get())
            CantidadEstado.config(text= "")
        except:
            CantidadEstado.config(text= "Valor invalido")
            return


        inventario.append([Nombre.get(), valor])
        ActualizarInventario(menuPrincipal)

def IniciarMenu(menuPrincipal):
        
        Nombre = tk.Entry(menuPrincipal,
            width= 15)
        Nombre.grid(row=3, column= 1)
        NombreEstado = tk.Label(menuPrincipal,
            width= 15, height= 1)
        NombreEstado.grid(row=4, column=1)

        Cantidad = tk.Entry(menuPrincipal,
            width= 15)
        Cantidad.grid(row= 5, column= 1)
        CantidadEstado = tk.Label(menuPrincipal,
            width= 15, height= 1)
        CantidadEstado.grid(row= 6, column= 1)

        BotonAgregar = tk.Button(menuPrincipal,
            text= "Agregar Producto", 
            width= 15, height= 2,
            command= partial(AgregarProducto, menuPrincipal, Nombre, NombreEstado, Cantidad, CantidadEstado))
        BotonAgregar.grid(row= 2, column= 1)

def ChecarOtrosProductosAntes(Nombre : tk.Entry):
    for i in range(len(inventario)):
        if (Nombre.get() == inventario[i][0]): return True
    return False   