import sqlite3
import os


class ConexionDB:
    def __init__(self):
        ruta_absoluta = os.path.abspath(__file__)
        directorio_actual = os.path.dirname(ruta_absoluta)
        self.base_datos = os.path.join(directorio_actual, '../database/peliculas.db')
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()