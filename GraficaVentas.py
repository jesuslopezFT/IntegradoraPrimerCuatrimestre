import ControlarInventario as inv
import Vender as vender
import tkinter as tk
from tkinter import messagebox  
from functools import partial
import matplotlib.pyplot as plt

# Función para mostrar la gráfica
def mostrar_grafica():
    plt.figure(figsize=(10, 6))

    plt.bar(inv.nombres_productos, inv.ventas_productos, color='skyblue')

    plt.title('Ventas de Productos', fontsize=14)
    plt.xlabel('Producto', fontsize=12)
    plt.ylabel('Número de Ventas', fontsize=12)

    plt.show()

def IniciarMenu(menuPrincipal):
    boton_grafica = tk.Button(menuPrincipal, text="Mostrar Gráfica de Ventas", command=mostrar_grafica)
    boton_grafica.grid(row=14, column=1)
