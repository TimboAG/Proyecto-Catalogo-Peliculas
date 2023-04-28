from .conexion_db import ConexionDB
from tkinter import messagebox
from .pelicula import Pelicula


def crear_tabla():
    conexion = ConexionDB()
    sql = '''  CREATE TABLE peliculas(
    id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre VARCHAR(100),
    duracion VARCHAR(10),
    genero VARCHAR(100)
    );
        '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "Se  creo  la tabla de la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Registro"
        mensaje = "La tabla ya esta creada"
        messagebox.showwarning(titulo, mensaje)


def eliminar_tabla():
    conexion = ConexionDB()
    sql = """
    DROP TABLE peliculas
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar Registro"
        mensaje = "Se  elimino la tabla de la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Borrar Registro"
        mensaje = "La tabla no existe"
        messagebox.showwarning(titulo, mensaje)


def guardar(pelicula):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla peliculas no esta creado en la base de datos'
        messagebox.showerror(titulo, mensaje)


def listar():
    conexion = ConexionDB()

    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro '
        mensaje = 'Crea la tabla en la Base de datos'
        messagebox.showwarning(titulo, mensaje)

    return lista_peliculas
