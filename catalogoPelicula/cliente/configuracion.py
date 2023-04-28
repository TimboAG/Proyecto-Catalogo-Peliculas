def habilitar_entry(self):
    self.entry_nombre.config(state="normal")
    self.entry_genero.config(state="normal")
    self.entry_duracion.config(state="normal")
    
def deshabilitar_entry(self):
    self.entry_nombre.config(state="normal")
    self.entry_genero.config(state="disabled")
    self.entry_duracion.config(state="disabled")
    
def habilitar_boton(self):
    self.boton_guardar.config(state="normal")
    self.boton_cancelar.config(state="normal")

def deshabilitar_boton(self):
    self.boton_guardar.config(state="disabled")
    self.boton_cancelar.config(state="disabled")