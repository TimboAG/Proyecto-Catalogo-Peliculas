import tkinter as tk
import cliente.configuracion as lab2   


def label_general(self,  nombre, rowL):
    self.label = tk.Label(self, text = nombre)
    self.label.config(font = ('Arial', 12, 'bold'), bg="#C3C3C3")
    self.label.grid(row = rowL, column = 0, padx = 10, pady = 10)

def entry_nombre(self):
    self.entry_nombre = tk.Entry(self)
    self.entry_nombre.config(width=50,  font=('Arial', 12))
    self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan = 2)    
    
def entry_genero(self):
    self.entry_genero = tk.Entry(self)
    self.entry_genero.config(width=50, font=('Arial', 12))
    self.entry_genero.grid(row=1, column=1, padx=10, pady=10, columnspan = 2)
        
def entry_duracion(self):
    self.entry_duracion = tk.Entry(self)
    self.entry_duracion.config(width=50,  font=('Arial', 12))
    self.entry_duracion.grid(row=2, column=1, padx=10, pady=10, columnspan = 2)
    
def boton_agregar(self):
        self.boton_agregar = tk.Button(self, text="Nuevo",  command= self.habilitar_entry)
        self.boton_agregar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#158645', 
                                cursor='hand2', activebackground='#35BD6F')
        self.boton_agregar.grid(row=3, column=0, padx=10, pady=10)
        
def boton_guardar(self):
        self.boton_guardar = tk.Button(self, text="Guardar")
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#1658A2', 
                                cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)
        
def boton_cancelar(self):
        self.boton_cancelar = tk.Button(self, text="Cancelar")
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#BD152E', 
                                cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)
        
        
# def habilitar_entry(self):
#     self.entry_nombre.config(state="disabled")
#     self.entry_genero.config(state="disabled")
#     self.entry_duracion.config(state="disabled")
def habilitar_entry(self):
    lab2.habilitar_entry(self)
    
def deshabilitar_entry(self):
    lab2.deshabilitar_entry(self)
    
def habilitar_boton(self):
    lab2.habilitar_boton(self)

def deshabilitar_boton(self):
    lab2.deshabilitar_boton(self)