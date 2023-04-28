from model.pelicula import Pelicula
from model.pelicula_dao import guardar, listar


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
    guardar(pelicula)
    deshabilitar_entry_y_deshabilitar_boton(self)


def listar_peliculas(self):
    return listar()
