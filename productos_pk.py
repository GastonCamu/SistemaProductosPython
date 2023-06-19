from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controlador_producto import *
import tkinter as tk
ventanas_abiertas=[]

def menu_productos():
    # Comando para borrar y ejecutar siguiente ventana
    def comando_compuesto():
        ventana.destroy()
        menu_productos()

    # Creacion de la ventana Mostrar Productos
    ventana = Tk()
    ventana.title("Productos")
        
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
    tabla['columns'] = ('Código','Descripción', 'Marca', 'Stock', 'Precio')

    # Configurar las columnas
    tabla.column('#0', width=0, stretch=NO)
    tabla.column('Código', anchor=CENTER, width=200)
    tabla.column('Descripción', anchor=CENTER, width=200)
    tabla.column('Marca', anchor=CENTER, width=100)
    tabla.column('Stock', anchor=CENTER, width=100)
    tabla.column('Precio', anchor=CENTER, width=100)

    # Agregar encabezados de columna
    tabla.heading('#0', text='')
    tabla.heading('Código', text='Código')  
    tabla.heading('Descripción', text='Descripción')
    tabla.heading('Marca', text='Marca')
    tabla.heading('Stock', text='Stock')
    tabla.heading('Precio', text='Precio')

    filas_productos = consultar_productos()
    for fila in filas_productos:
        tabla.insert(parent='', index='end', iid=fila[0], text='', values=(fila[0],fila[1], fila[2], fila[3], fila[4]))

    tabla.pack()


    def i_insertar_producto():
        ventana.destroy()
    # Comando para borrar y ejecutar siguiente ventana
        def comando_compuesto():
            ventana2.destroy()
            menu_productos()

        def cargar_datos():
            codigo = entryCod_prod.get()
            descripcion = entryDescrip.get()
            marca = entryMarca.get()
            stock = entryStock.get()
            precio = entryPrecio.get()

            if codigo and descripcion and marca and stock and precio:
                # Llamar a la función para crear el producto
                insertar_producto(codigo, descripcion, marca, stock, precio)
                messagebox.showinfo(message="Producto insertado correctamente")
                # Ejecutar el comando compuesto para cerrar la ventana2 actual y volver al menú de productos
                comando_compuesto()
            else:
                messagebox.showwarning(message="Por favor, complete todos los campos")

        # Creación de la ventana2 Insertar Productos
        ventana2 = Tk()
        ventana2.title("Insertar Productos")
        

        # Tamaño de la ventana2
        ancho_ventana2 = 800
        alto_ventana2 = 500
        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = ventana2.winfo_screenwidth()
        alto_pantalla = ventana2.winfo_screenheight()
        # Calcular las coordenadas para centrar la ventana2
        x = (ancho_pantalla // 2) - (ancho_ventana2 // 2)
        y = (alto_pantalla // 2) - (alto_ventana2 // 2) - 50
        # Establecer la geometría de la ventana2
        ventana2.geometry(f"{ancho_ventana2}x{alto_ventana2}+{x}+{y}")

        frameInsertar = Frame(ventana2)
        frameInsertar.pack(padx=30, pady=30)

        # Código del producto
        LabelCod_prod = Label(frameInsertar, text="Código del producto:")
        LabelCod_prod.config(font=40)
        LabelCod_prod.grid(row=0, column=0, padx=30, pady=2)
        entryCod_prod = Entry(frameInsertar, width=40)
        entryCod_prod.grid(row=0, column=1)

        # Descripción del producto
        LabelDescrip = Label(frameInsertar, text="Descripción del producto:")
        LabelDescrip.config(font=40)
        LabelDescrip.grid(row=1, column=0, padx=30, pady=2)
        entryDescrip = Entry(frameInsertar, width=40)
        entryDescrip.grid(row=1, column=1)

        # Marca del producto
        LabelMarca = Label(frameInsertar, text="Marca:")
        LabelMarca.config(font=40)
        LabelMarca.grid(row=2, column=0, padx=30, pady=2)
        entryMarca = Entry(frameInsertar, width=40)
        entryMarca.grid(row=2, column=1)

        # Stock del producto
        LabelStock = Label(frameInsertar, text="Stock:")
        LabelStock.config(font=40)
        LabelStock.grid(row=3, column=0, padx=30, pady=2)
        entryStock = Entry(frameInsertar, width=40)
        entryStock.grid(row=3, column=1)

        # Precio del producto
        LabelPrecio = Label(frameInsertar, text="Precio:")
        LabelPrecio.config(font=40)
        LabelPrecio.grid(row=4, column=0, padx=30, pady=2)
        entryPrecio = Entry(frameInsertar, width=40)
        entryPrecio.grid(row=4, column=1)

        btn_cargar = Button(frameInsertar, text="Cargar", command=cargar_datos)
        btn_cargar.config(width=20)
        btn_cargar.grid(row=5, columnspan=2, pady=10)

        btn_salir = Button(frameInsertar, text="Volver", command=comando_compuesto)
        btn_salir.config(width=20)
        btn_salir.grid(row=6, columnspan=2, pady=10)

        # Función para cerrar la ventana2 al presionar la 'x'
        ventana2.protocol("WM_DELETE_WINDOW", comando_compuesto)

        ventana2.mainloop()


    def i_eliminar_producto():
        # Obtener el elemento seleccionado en la tabla
        seleccionado = tabla.focus()
        if seleccionado:
            # Obtener los valores de las columnas del elemento seleccionado
            valores = tabla.item(seleccionado)['values']
            
            # Confirmar la eliminación con un cuadro de diálogo
            confirmar = tk.messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar el producto '{valores[0]}'?")
            if confirmar:
                # Eliminar el elemento de la tabla
                eliminar_producto(valores[0])
                tk.messagebox.showinfo("Eliminado", "El producto ha sido eliminado correctamente.")
                ventana.destroy()
                menu_productos()
        else:
            tk.messagebox.showwarning("Seleccionar producto", "Por favor, selecciona un producto de la tabla.")




    btn_insertar = Button(framePrincipal, text="Insertar", command=i_insertar_producto)
    btn_insertar.config(width=20)
    btn_insertar.pack(padx=42,pady=15,side="left")
    btn_Eliminar = Button(framePrincipal, text="Eliminar", command=i_eliminar_producto)
    btn_Eliminar.config(width=20)
    btn_Eliminar.pack(padx=42,pady=15,side="left")
    btn_salir = Button(framePrincipal, text="Salir", command=ventana.destroy)
    btn_salir.config(width=20)
    btn_salir.pack(padx=42,pady=15,side="left")

    ventana.mainloop()



