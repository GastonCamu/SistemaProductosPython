from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controlador_producto import *
import tkinter as tk
ventanas_abiertas=[]

# Ventana del menu de productos
def menu_productos():
    # Funcion para cerrar la ventana y abrir el menu de productos a la vez
    def comando_compuesto():
        ventana.destroy()
        menu_productos()

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

    # Ventana para insertar productos
    def i_insertar_producto():
        ventana.destroy()
    # Funcion para cerrar la ventana y abrir el menu de productos a la vez
        def comando_compuesto():
            ventana2.destroy()
            menu_productos()

        # Funcion que sirve para cargar los datos de los productos en la bd
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

        # Creación de la ventana2 para Insertar Productos
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

        # Boton para cargar los datos
        btn_cargar = Button(frameInsertar, text="Cargar", command=cargar_datos)
        btn_cargar.config(width=20)
        btn_cargar.grid(row=5, columnspan=2, pady=10)

        # Boton para volver al menu de productos
        btn_salir = Button(frameInsertar, text="Volver", command=comando_compuesto)
        btn_salir.config(width=20)
        btn_salir.grid(row=6, columnspan=2, pady=10)

        # Función para cerrar la ventana2 al presionar la 'x'
        ventana2.protocol("WM_DELETE_WINDOW", comando_compuesto)

        ventana2.mainloop()

    # Ventana para modificar los productos
    def i_modificar_producto(cod_prod,descrip_prod,marca_prod,stock_prod,precio_prod):
        ventana.destroy()
        # Funcion para cerrar la ventana y abrir a la vez el menu de productos
        def comando_compuesto():
            ventana3.destroy()
            menu_productos()

        # Funcion para cargar los cambios de los productos
        def cargar_datos():
            codigo = cod_prod
            descripcion = entryDescrip.get()
            marca = entryMarca.get()
            stock = entryStock.get()
            precio = entryPrecio.get()

            if codigo and descripcion and marca and stock and precio:
                # Llamar a la función para modificar el producto
                modificar_producto(codigo, descripcion, marca, stock, precio)
                messagebox.showinfo(message="Producto modificado correctamente")
                # Ejecutar el comando compuesto para cerrar la ventana3 actual
                comando_compuesto()
            else:
                messagebox.showwarning(message="Por favor, complete todos los campos")

        # Creación de la ventana3 modificar un producto
        ventana3 = Tk()
        ventana3.title("Modificar un producto")
        

        # Tamaño de la ventana3
        ancho_ventana3 = 800
        alto_ventana3 = 500
        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = ventana3.winfo_screenwidth()
        alto_pantalla = ventana3.winfo_screenheight()
        # Calcular las coordenadas para centrar la ventana3
        x = (ancho_pantalla // 2) - (ancho_ventana3 // 2)
        y = (alto_pantalla // 2) - (alto_ventana3 // 2) - 50
        # Establecer la geometría de la ventana3
        ventana3.geometry(f"{ancho_ventana3}x{alto_ventana3}+{x}+{y}")

        frameModificar = Frame(ventana3)
        frameModificar.pack(padx=30, pady=30)

        # Descripción del producto
        LabelDescrip = Label(frameModificar, text="Descripción del producto:")
        LabelDescrip.config(font=40)
        LabelDescrip.grid(row=1, column=0, padx=30, pady=2)
        entryDescrip = Entry(frameModificar, width=40)
        entryDescrip.insert(0,descrip_prod)
        entryDescrip.grid(row=1, column=1)

        # Marca del producto
        LabelMarca = Label(frameModificar, text="Marca:")
        LabelMarca.config(font=40)
        LabelMarca.grid(row=2, column=0, padx=30, pady=2)
        entryMarca = Entry(frameModificar, width=40)
        entryMarca.insert(0,marca_prod)
        entryMarca.grid(row=2, column=1)

        # Stock del producto
        LabelStock = Label(frameModificar, text="Stock:")
        LabelStock.config(font=40)
        LabelStock.grid(row=3, column=0, padx=30, pady=2)
        entryStock = Entry(frameModificar, width=40)
        entryStock.insert(0,stock_prod)
        entryStock.grid(row=3, column=1)

        # Precio del producto
        LabelPrecio = Label(frameModificar, text="Precio:")
        LabelPrecio.config(font=40)
        LabelPrecio.grid(row=4, column=0, padx=30, pady=2)
        entryPrecio = Entry(frameModificar, width=40)
        entryPrecio.insert(0,precio_prod)
        entryPrecio.grid(row=4, column=1)

        # Boton para guardar los cambios de los productos
        btn_cargar = Button(frameModificar, text="Guardar", command=cargar_datos)
        btn_cargar.config(width=20)
        btn_cargar.grid(row=5, columnspan=2, pady=10)

        # Boton para volver al menu de productos
        btn_salir = Button(frameModificar, text="Volver", command=comando_compuesto)
        btn_salir.config(width=20)
        btn_salir.grid(row=6, columnspan=2, pady=10)

        # Función para cerrar la ventana3 al presionar la 'x'
        ventana3.protocol("WM_DELETE_WINDOW", comando_compuesto)

        ventana3.mainloop()

    # Funcion para seleccionar el producto y transferir los datos a la ventana de modificar productos
    def c_modificar_producto():
        # Obtener el elemento seleccionado en la tabla
        seleccionado = tabla.focus()
        if seleccionado:
            # Obtener los valores de las columnas del elemento seleccionado
            valores = tabla.item(seleccionado)['values']
            
            # Confirmar la modificacion con un cuadro de diálogo
            confirmar = tk.messagebox.askyesno("Confirmar modificación", f"¿Estás seguro que desea modificar el producto '{valores[0]}'?")
            if confirmar:
                # Modificar el elemento de la tabla
                
                i_modificar_producto(valores[0],valores[1],valores[2],valores[3],valores[4])
                ventana.destroy()
                menu_productos()
        else:
            tk.messagebox.showwarning("Seleccionar producto", "Por favor, selecciona un producto de la tabla.")

    # Ventana para eliminar productos
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

    # Boton para insertar un producto
    btn_insertar = Button(framePrincipal, text="Insertar", command=i_insertar_producto)
    btn_insertar.config(width=20)
    btn_insertar.pack(padx=12,pady=15,side="left")
    
    # Boton para modificar un producto
    btn_Modificar = Button(framePrincipal, text="Modificar", command=c_modificar_producto)
    btn_Modificar.config(width=20)
    btn_Modificar.pack(padx=12,pady=15,side="left")
    
    # Boton para eliminar un producto
    btn_Eliminar = Button(framePrincipal, text="Eliminar", command=i_eliminar_producto)
    btn_Eliminar.config(width=20)
    btn_Eliminar.pack(padx=12,pady=15,side="left")
    
    # Boton para salir del sistema
    btn_salir = Button(framePrincipal, text="Salir", command=ventana.destroy)
    btn_salir.config(width=20)
    btn_salir.pack(padx=12,pady=15,side="left")

    ventana.mainloop()



