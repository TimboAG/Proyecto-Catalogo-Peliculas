import tkinter as tk
import cliente.componentes as lab   
import cliente.configuracion as lab2   

class Frame(tk.Frame):
    
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320 )
        self.root = root
        self.pack()
        self.config( bg="#C3C3C3")
        self.campo_pelicula()
        self.entrys_pelicula()
        self.botones_pelicula()
        #lab2.deshabilitar_entry(self)   
        
    def campo_pelicula(self):
        lab.label_general(self, nombre="Nombre", rowL=0)
        lab.label_general(self, nombre="Genero", rowL=1)
        lab.label_general(self, nombre="Duracion", rowL=2)
    
    def entrys_pelicula(self):
        lab.entry_nombre(self)
        lab.entry_genero(self )
        lab.entry_duracion(self)
        
    def botones_pelicula(self):
        lab.boton_agregar(self)
        lab.boton_cancelar(self )
        lab.boton_guardar(self)

    

