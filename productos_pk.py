from tkinter import *
from tkinter import ttk
from controlador_producto import *

def i_mostrar_productos():
    # Comando para borrar y ejecutar siguiente ventana
    def comando_compuesto():
        ventana.destroy()
        menu_productos()

    # Creacion de la ventana Mostrar Productos
    ventana = Tk()
    ventana.title("Mostrar Productos")
    
    # Tamaño de la ventana
    ancho_ventana = 800
    alto_ventana = 500
    # Obtener el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2) - 50
    # Establecer la geometría de la ventana
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


    framePrincipal = Frame(ventana)
    framePrincipal.pack()
    
    # Crear Treeview para mostrar la tabla
    tabla = ttk.Treeview(framePrincipal)
    tabla['columns'] = ('Descripción', 'Marca', 'Stock', 'Precio')

    # Configurar las columnas
    tabla.column('#0', width=0, stretch=NO)
    tabla.column('Descripción', anchor=CENTER, width=200)
    tabla.column('Marca', anchor=CENTER, width=100)
    tabla.column('Stock', anchor=CENTER, width=100)
    tabla.column('Precio', anchor=CENTER, width=100)

    # Agregar encabezados de columna
    tabla.heading('#0', text='')
    tabla.heading('Descripción', text='Descripción')
    tabla.heading('Marca', text='Marca')
    tabla.heading('Stock', text='Stock')
    tabla.heading('Precio', text='Precio')

    filas_productos = consultar_productos()
    for fila in filas_productos:
        tabla.insert(parent='', index='end', iid=fila[0], text='', values=(fila[1], fila[2], fila[3], fila[4]))

    tabla.pack()

    btn_salir = Button(framePrincipal, text="Salir", command=comando_compuesto)
    btn_salir.config(width=20)
    btn_salir.pack()

    ventana.mainloop()



def menu_productos():
    # Comando para borrar y ejecutar siguiente ventana
    def comando_compuesto():
        ventana.destroy()
        i_mostrar_productos()

    # Creacion de la ventana Menu Productos  
    ventana = Tk()
    ventana.title("Menu Productos")
    
    # Tamaño de la ventana
    ancho_ventana = 300
    alto_ventana = 500
    # Obtener el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2) - 50
    # Establecer la geometría de la ventana
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    framePrincipal = Frame(ventana)
    framePrincipal.pack()

    btn_mostrar_t = Button(framePrincipal, text="Mostrar productos", command=comando_compuesto)
    btn_mostrar_t.config(width=20, height=4)
    btn_mostrar_t.grid(row=0)

    btn_insertar = Button(framePrincipal, text="Insertar un producto")
    btn_insertar.config(width=20, height=4)
    btn_insertar.grid(row=1)

    btn_modificar = Button(framePrincipal, text="Modificar un producto")
    btn_modificar.config(width=20, height=4)
    btn_modificar.grid(row=2)

    btn_borrar = Button(framePrincipal, text="Borrar un producto")
    btn_borrar.config(width=20, height=4)
    btn_borrar.grid(row=3)

    btn_salir = Button(framePrincipal, text="Salir", command=ventana.destroy)
    btn_salir.config(width=20)
    btn_salir.grid(row=4)

    for i in framePrincipal.winfo_children():
        i.grid_configure(padx=12, pady=12)

    ventana.mainloop()
