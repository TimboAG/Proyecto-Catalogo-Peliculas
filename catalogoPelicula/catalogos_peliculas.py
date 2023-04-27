import tkinter as tk
import os

def main():
    root = tk.Tk()
    root.title("Catalogo de Peliculas")
    ruta_icono = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img', 'logo.ico'))
    root.iconbitmap(ruta_icono)
    root.mainloop()

if __name__ == "__main__":
    main()