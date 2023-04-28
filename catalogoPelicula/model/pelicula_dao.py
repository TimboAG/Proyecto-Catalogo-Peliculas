from .conexion_db import ConexionDB

def crear_tabla():
    conexion = ConexionDB()
    sql= '''  CREATE TABLE peliculas(
    id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre VARCHAR(100),
    duracion VARCHAR(10),
    genero VARCHAR(100)
    );
        '''
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
def eliminar_tabla():
    conexion = ConexionDB()
    sql= """
    DROP TABLE peliculas
    """  
    conexion.cursor.execute(sql)
    conexion.cerrar()
    