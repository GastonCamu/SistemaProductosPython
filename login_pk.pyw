from tkinter import *
from controlador_usuario import *

# Creacion de la ventana login
ventana=Tk()
ventana.title("Inicio de Sesion")
ventana.geometry("500x300")
framePrincipal=Frame(ventana)
framePrincipal.pack()

# Usuario del login
LabelUser=Label(framePrincipal,text="Usuario:")
LabelUser.config(font=40)
LabelUser.grid(row=0,column=0)
entryUser=Entry(framePrincipal,width=10)
entryUser.grid(row=0,column=1)

# Contraseña del login
LabelPass=Label(framePrincipal,text="Contraseña:")
LabelPass.grid(row=1,column=0)
LabelPass.config(font=40)
entryPass=Entry(framePrincipal,width=10)
entryPass.config(show="#")
entryPass.grid(row=1,column=1)

def login():
    verificar_usuario(entryUser.get(),entryPass.get())

# Boton para ingresar al sistema principal 
btnEnter= Button(framePrincipal,text="Ingresar")
btnEnter.config(width=10,command=login)
btnEnter.grid(row=2,column=0)

# Boton para salir del sistema
btnSalir= Button(framePrincipal,text="Salir")
btnSalir.config(width=10,command=ventana.quit)
btnSalir.grid(row=2,column=1)


ventana.mainloop()
