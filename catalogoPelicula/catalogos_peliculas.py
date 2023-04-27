import tkinter as tk
import os
from cliente.gui_app import Frame
from cliente.menu import menu

def main():
    root = tk.Tk()
    root.title("Catalogo de Peliculas")
    ruta_icono = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img', 'logo.ico'))
    root.iconbitmap(ruta_icono)
    #hago que la ventana no pueda estirarse o alargarse, sino que quede un un ancho y largo fijo resizable(0,0) los 0 son de False, el primer 0 es el de los costados y el seguno 0 es hacia abajo
    root.resizable(0,0)
    # #con frame genero el contenedor de los elementos,   luego lo empaqueto
    # frame= tk.Frame(root)
    # frame.pack()
    # #genero el tamaño de mi ventanay bg el color del fondo
    # frame.config(width=480, height=320, bg="black")
    menu(root)
    app= Frame(root=root)
    app.mainloop()

if __name__ == "__main__":
    main()