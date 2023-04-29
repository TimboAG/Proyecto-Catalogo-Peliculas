from model.pelicula import Pelicula
from model.pelicula_dao import guardar, listar, editar, eliminar
from tkinter import messagebox


def habilitar_entry(self):
    self.entry_nombre.config(state="normal")
    self.entry_duracion.config(state="normal")
    self.entry_genero.config(state="normal")


def deshabilitar_entry(self):
    self.entry_nombre.config(state="disabled")
    self.entry_genero.config(state="disabled")
    self.entry_duracion.config(state="disabled")


def habilitar_boton(self):
    self.boton_guardar.config(state="normal")
    self.boton_cancelar.config(state="normal")


def deshabilitar_boton(self):
    self.boton_guardar.config(state="disabled")
    self.boton_cancelar.config(state="disabled")


def habilitar_entry_y_habilitar_boton(self):
    self.mi_nombre.set('')
    self.mi_duracion.set('')
    self.mi_genero.set('')
    self.habilitar_entry()
    self.habilitar_boton()


def deshabilitar_entry_y_deshabilitar_boton(self):
    self.deshabilitar_entry()
    self.deshabilitar_boton()
    self.mi_nombre.set('')
    self.mi_duracion.set('')
    self.mi_genero.set('')


def guardar_datos(self):
    pelicula = Pelicula(
        self.mi_nombre.get(),
        self.mi_duracion.get(),
        self.mi_genero.get()
    )
    if self.id_pelicula == None:
        guardar(pelicula)
        limpiar(self)
        deshabilitar_entry_y_deshabilitar_boton(self)
    else:
        editar(pelicula, self.id_pelicula)
        deshabilitar_entry_y_deshabilitar_boton(self)
        limpiar(self)


def listar_peliculas(self):
    return listar()


def editar_datos(self):
    try:
        self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
        self.nombre_pelicula = self.tabla.item(
            self.tabla.selection())['values'][0]
        self.duracion_pelicula = self.tabla.item(
            self.tabla.selection())['values'][1]
        self.genero_pelicula = self.tabla.item(
            self.tabla.selection())['values'][2]
        habilitar_entry_y_habilitar_boton(self)
        self.entry_nombre.insert(0, self.nombre_pelicula)
        self.entry_genero.insert(0, self.genero_pelicula)
        self.entry_duracion.insert(0, self.duracion_pelicula)
        self.tabla_peliculas()
    except:
        titulo = 'Edición de datos'
        mensaje = 'No ha seleccionado nigun registro'
        messagebox.showerror(titulo, mensaje)
        limpiar(self)


def eliminar_datos(self):
    try:
        self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
        eliminar(self.id_pelicula)
        self.tabla_peliculas()
        limpiar(self)
    except:
        titulo = 'Eliminar un Registro'
        mensaje = 'No ha seleccionado nigun registro'
        messagebox.showerror(titulo, mensaje)


def limpiar(self):
    peliculas = listar_peliculas(self)
    self.tabla.delete(*self.tabla.get_children())
    for pelicula in peliculas:
        self.tabla.insert('', 'end', text=pelicula[0], values=(
            pelicula[1], pelicula[2], pelicula[3]))
