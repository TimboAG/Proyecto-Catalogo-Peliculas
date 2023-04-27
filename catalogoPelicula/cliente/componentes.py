import tkinter as tk


def label_general(self,  nombre, rowL):
    self.label = tk.Label(self, text = nombre)
    self.label.config(font = ('Arial', 12, 'bold'))
    self.label.grid(row = rowL, column = 0, padx = 10, pady = 10)

def entry_nombre(self, columL, rowL):
    self.entry_nombre = tk.Entry(self)
    self.entry_nombre.config(width=50, state= "disable", font=('Arial', 12))
    self.entry_nombre.grid(row=rowL, column=columL, padx=10, pady=10)    
    
def entry_genero(self, columL, rowL):
    self.entry_genero = tk.Entry(self)
    self.entry_genero.config(width=50, state= "disable", font=('Arial', 12))
    self.entry_genero.grid(row=rowL, column=columL, padx=10, pady=10)
        
def entry_duracion(self, columL, rowL):
    self.entry_duracion = tk.Entry(self)
    self.entry_duracion.config(width=50, state= "disable", font=('Arial', 12))
    self.entry_duracion.grid(row=rowL, column=columL, padx=10, pady=10)