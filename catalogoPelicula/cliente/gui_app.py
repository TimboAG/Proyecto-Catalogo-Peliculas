import tkinter as tk
import cliente.componentes as lab
from model.pelicula import Pelicula


class Frame(tk.Frame):

    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="#C3C3C3")
        self.id_pelicula = None
        self.campo_pelicula()
        self.entrys_pelicula()
        self.botones_pelicula()
        self.deshabilitar_entry()
        self.deshabilitar_boton()
        self.tabla_peliculas()

    def campo_pelicula(self):
        lab.label_general(self, nombre="Nombre", rowL=0)
        lab.label_general(self, nombre="Genero", rowL=1)
        lab.label_general(self, nombre="Duracion", rowL=2)

    def entrys_pelicula(self):
        lab.entry_nombre(self)
        lab.entry_genero(self)
        lab.entry_duracion(self)

    def botones_pelicula(self):
        lab.boton_agregar(self)
        lab.boton_cancelar(self)
        lab.boton_guardar(self)

    def tabla_peliculas(self):
        lab.tabla_peliculas(self)

    def habilitar_entry(self):
        lab.habilitar_entry(self)

    def deshabilitar_entry(self):
        lab.deshabilitar_entry(self)

    def habilitar_boton(self):
        lab.habilitar_boton(self)

    def deshabilitar_boton(self):
        lab.deshabilitar_boton(self)

    def habilitar_entry_y_habilitar_boton(self):
        lab.habilitar_entry_y_habilitar_boton(self)

    def deshabilitar_entry_y_deshabilitar_boton(self):
        lab.deshabilitar_entry_y_deshabilitar_boton(self)

    def guardar_datos(self):
        lab.guardar_datos(self)

    def editar_datos(self):
        lab.editar_datos(self)

    def eliminar_datos(self):
        lab.eliminar_datos(self)
