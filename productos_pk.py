from tkinter import *
from controlador_producto import *
def i_mostrar_productos():
    # Comando para borrar y ejecutar siguiente ventana
    def comando_compuesto():
        ventana.destroy()
        menu_productos()
        
    # Creacion de la ventana Mostrar Productos
    ventana=Tk()
    ventana.title("Mostrar Productos")
    ventana.geometry("800x500")
    framePrincipal=Frame(ventana)
    framePrincipal.pack()
    visual_text = Label(framePrincipal)
    visual_text.grid(row=0)
    filas_productos = consultar_productos()
    visual_text["text"] = filas_productos
    btn_salir = Button(framePrincipal,text="Salir")
    btn_salir.config(width=20,command=comando_compuesto)
    btn_salir.grid(row=4)


    ventana.mainloop()

def menu_productos():
    # Comando para borrar y ejecutar siguiente ventana
    def comando_compuesto():
        ventana.destroy()
        i_mostrar_productos()
        
    # Creacion de la ventana Menu Productos  
    ventana=Tk()
    ventana.title("Menu Productos")
    ventana.geometry("300x500")

    framePrincipal=Frame(ventana)
    framePrincipal.pack()

    btn_mostrar_t = Button(framePrincipal,text="Mostrar productos")
    btn_mostrar_t.config(width=20,height=4,command=comando_compuesto)
    btn_mostrar_t.grid(row=0)

    btn_insertar = Button(framePrincipal,text="Insertar un producto")
    btn_insertar.config(width=20,height=4)
    btn_insertar.grid(row=1)

    btn_modificar = Button(framePrincipal,text="Modificar un producto")
    btn_modificar.config(width=20,height=4)
    btn_modificar.grid(row=2)

    btn_borrar = Button(framePrincipal,text="Borrar un producto")
    btn_borrar.config(width=20,height=4)
    btn_borrar.grid(row=3)

    btn_salir = Button(framePrincipal,text="Salir")
    btn_salir.config(width=20,command=ventana.quit)
    btn_salir.grid(row=4)

    for i in framePrincipal.winfo_children():
        i.grid_configure(padx=12, pady=12)


    ventana.mainloop()

menu_productos()