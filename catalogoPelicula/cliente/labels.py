import tkinter as tk

def label_nombre(self):
     nombre="Nombre"
     rowL=0
     label_general(self, nombre, rowL)
          
def label_duracion(self):
     nombre="Duracion"
     rowL=1
     label_general(self, nombre, rowL)
     
def label_genero(self):
     nombre="Genero"
     rowL=2
     label_general(self, nombre, rowL)
     
def label_general(self,  nombre, rowL):
     self.label = tk.Label(self, text = nombre)
     self.label.config(font = ('Arial', 12, 'bold'))
     self.label.grid(row = rowL, column = 0, padx = 10, pady = 10)