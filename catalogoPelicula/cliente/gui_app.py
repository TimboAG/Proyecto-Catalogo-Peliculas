import tkinter as tk
import cliente.componentes as lab   

class Frame(tk.Frame):
    
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320 )
        self.root = root
        self.pack()
        self.config( bg="black")
        self.campo_pelicula()
        self.entrys_pelicula()
        
        
    def campo_pelicula(self):
        lab.label_general(self, nombre="Nombre", rowL=0)
        lab.label_general(self, nombre="Genero", rowL=1)
        lab.label_general(self, nombre="Duracion", rowL=2)
    
    def entrys_pelicula(self):
        lab.entry_nombre(self, columL= 1, rowL=0)
        lab.entry_genero(self, columL= 1, rowL=1 )
        lab.entry_duracion(self, columL=1, rowL=2 )

    

