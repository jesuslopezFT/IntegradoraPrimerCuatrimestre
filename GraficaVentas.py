import ControlarInventario as inventario
import tkinter as tk
from tkinter import messagebox  
from functools import partial
import matplotlib.pyplot as plt

# Crear la gráfica de ventas
plt.figure(figsize=(10, 6))  # Tamaño de la figura (opcional)

# Crear gráfico de barras
plt.bar(inventario.nombres_productos, inventario.ventas_productos, color='skyblue')

# Añadir título y etiquetas
plt.title('Ventas de Productos', fontsize=14)
plt.xlabel('Producto', fontsize=12)
plt.ylabel('Número de Ventas', fontsize=12)

# Mostrar la gráfica
plt.show()