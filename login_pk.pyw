from tkinter import *
from tkinter import messagebox
from controlador_usuario import verificar_usuario
from productos_pk import menu_productos

# Creacion de la ventana login
ventana=Tk()
ventana.title("Inicio de Sesion")

# Tamaño de la ventana
ancho_ventana = 500
alto_ventana = 300
# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2) - 50
# Establecer la geometría de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

frameLogin=Frame(ventana)
frameLogin.pack()

def comando_compuesto():
        ventana.destroy()
        menu_productos()
        
# Usuario del login
LabelUser=Label(frameLogin,text="Usuario:")
LabelUser.config(font=40)
LabelUser.grid(row=0,column=0)
entryUser=Entry(frameLogin,width=10)
entryUser.grid(row=0,column=1)

# Contraseña del login
LabelPass=Label(frameLogin,text="Contraseña:")
LabelPass.grid(row=1,column=0)
LabelPass.config(font=40)
entryPass=Entry(frameLogin,width=10)
entryPass.config(show="#")
entryPass.grid(row=1,column=1)

def login():
    respuesta = verificar_usuario(entryUser.get(),entryPass.get())
    if respuesta == True:
        comando_compuesto()
    else:
        messagebox.showwarning(message="USUARIO O CONTRASEÑA INCORRECTA")
        if messagebox.OK:
            ventana.destroy()
# Boton para ingresar al sistema principal 
btnEnter= Button(frameLogin,text="Ingresar")
btnEnter.config(width=10,command=login)
btnEnter.grid(row=2,column=0)

# Boton para salir del sistema
btnSalir= Button(frameLogin,text="Salir")
btnSalir.config(width=10,command=ventana.quit)
btnSalir.grid(row=2,column=1)


ventana.mainloop()
