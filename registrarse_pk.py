from tkinter import *
from tkinter import messagebox
from controlador_usuario import crear_usuario

# Ventana para registrarse
def ventana_registro():
    ventana=Tk()
    ventana.title("Registrarse")

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

    frameRegistro=Frame(ventana)
    frameRegistro.pack(padx=30,pady=30)
    
    # Funcion para cargar los datos del usuario en la bd
    def cargar_datos():
        #AQUI CREAR_USUARIO EMPEZABA CON 5 SETEANDOLE ESE VALOR POR DEFECTO AL COD_USUARIO, A LA PK, ya lo saqué y modifiqué el controlador y el modelo
        crear_usuario(entryUsername.get(),entryNombre.get(),entryApellido.get(),entryDni.get(),entryPass.get())
        messagebox.showinfo(message="Registro exitoso")
        if messagebox.OK:
            ventana.destroy()
            
    # Usuario del registro
    LabelUsername=Label(frameRegistro,text="Usuario:")
    LabelUsername.config(font=40)
    LabelUsername.grid(row=0,column=0,padx=30,pady=2)
    entryUsername=Entry(frameRegistro,width=40)
    entryUsername.grid(row=0,column=1)
    
    # Nombre del registro
    LabelNombre=Label(frameRegistro,text="Nombre:")
    LabelNombre.config(font=40)
    LabelNombre.grid(row=1,column=0,padx=30,pady=2)
    entryNombre=Entry(frameRegistro,width=40)
    entryNombre.grid(row=1,column=1)
    
    # Apellido del registro
    LabelApellido=Label(frameRegistro,text="Apellido:")
    LabelApellido.config(font=40)
    LabelApellido.grid(row=2,column=0,padx=30,pady=2)
    entryApellido=Entry(frameRegistro,width=40)
    entryApellido.grid(row=2,column=1)

    # Dni del registro
    LabelDni=Label(frameRegistro,text="DNI:")
    LabelDni.config(font=40)
    LabelDni.grid(row=3,column=0,padx=30,pady=2)
    entryDni=Entry(frameRegistro,width=40)
    entryDni.grid(row=3,column=1)

    # Contraseña del registro
    LabelPass=Label(frameRegistro,text="Contraseña:")
    LabelPass.grid(row=4,column=0,padx=30,pady=2)
    LabelPass.config(font=40)
    entryPass=Entry(frameRegistro,width=40)
    entryPass.grid(row=4,column=1)

    # Boton para cargar datos
    btnEnter=Button(frameRegistro,text="Enviar")
    btnEnter.config(width=15,command=cargar_datos)
    btnEnter.grid(row=5,column=0,pady=10,padx=40)

    # Boton para regresar a la ventana principal
    btnSalir=Button(frameRegistro,text="Volver")
    btnSalir.config(width=15,command=ventana.destroy)
    btnSalir.grid(row=5,column=1,pady=10,padx=40)


    ventana.mainloop()
