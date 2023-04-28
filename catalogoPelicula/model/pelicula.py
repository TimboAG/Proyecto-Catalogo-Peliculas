class Pelicula:
    __nombre: None
    __genero = None
    __duracion = None

    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.genero = genero

    def get_duracion(self):
        return self.__duracion

    def set_duracion(self, duracion):
        self.duracion = duracion

    def __str__(self):
        return f'Pelicila[{self.nombre}, {self.duracion}, {self.genero}]'
