import tkinter as tk

def menu(root):
    menu=tk.Menu(root)
    root.config(menu= menu, width=300, height=300, bg="#CBCBCB")
    menu_inicio(menu, root)
    menu_ayuda(menu)
    
    
def  menu_inicio(menu, root):
    #tearrof=0 me quita los espacios que se generaban y unas lineas en ese espacio
    inicio=tk.Menu(menu, tearoff=0)
    menu.add_cascade(label = "Inicio", menu =inicio )
    inicio.add_command(label = "Crear un registro en la db")
    inicio.add_command(label = "Eliminar un registro de la db")
    inicio.add_command(label = "Salir", command= root.destroy)
    
def  menu_ayuda(menu):
        #tearrof=0 me quita los espacios que se generaban y unas lineas en ese espacio
    ayuda=tk.Menu(menu, tearoff=0)
    menu.add_cascade(label = "Ayuda", menu =ayuda )
    ayuda.add_command(label = "Como usar la aplicacion")
    ayuda.add_command(label = "Version")
    ayuda.add_command(label = "Nosotros")