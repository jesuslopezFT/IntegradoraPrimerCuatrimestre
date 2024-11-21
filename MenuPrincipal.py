

import tkinter as tk


# Funciones
def prueba():
    Boton = tk.Button(menuPrincipal, text= "?", width= 25, height= 3)
    Boton.grid(row= 2, column= 25)

def main():
    while True:
        for i in range(len(inventario)):
            print(i)




# Tkinter
menuPrincipal = tk.Tk()
menuPrincipal.title("Control de Inventario")

Titulo = tk.Label(menuPrincipal, text= "Control de Inventario", width= 25)
Titulo.grid(row= 1, column= 1)

BotonAgregar = tk.Button(menuPrincipal, text= "Agregar Producto", width= 15, command= prueba)
BotonAgregar.grid(row= 2, column= 1)

menuPrincipal.mainloop()

if __name__ == "__main__":
    main()