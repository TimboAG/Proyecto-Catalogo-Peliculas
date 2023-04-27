import tkinter as tk
import cliente.labels as lab   

class Frame(tk.Frame):
    
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320 )
        self.root = root
        self.pack()
        self.config( bg="black")
        self.campo_pelicula()
        
        
    def campo_pelicula(self):
        lab.label_nombre(self)
        lab.label_genero(self)
        lab.label_duracion(self)
    
    

