from conexion import ConexionDB
from modelo_producto import Producto

# Funcion para insertar un producto
def insertar_producto():
    
    # Ingreso de datos por el usuario.
    cod_prod=int(input("Ingrese el código del producto: "))
    descrip_prod=input("Descripción: ")
    cod_marca=int(input("Ingrese el código de la marca: "))
    stock=int(input("Stock: "))
    precio=float(input("Precio en pesos argentinos: $"))
    producto=Producto(cod_prod,descrip_prod,cod_marca,stock,precio)
    
    # Carga de productos en la base de datos
    db=ConexionDB("practico_evaluativo.db")
    request=f"insert into PRODUCTOS values({producto.cod_prod},'{producto.descrip_prod}',{producto.cod_marca},{producto.stock},{producto.precio})"
    db.request(request)
    db.commit()
    db.db_close()

# Funcion para consultar todos los productos
def consultar_productos():
    db=ConexionDB("practico_evaluativo.db")
    request=f"select * from PRODUCTOS"
    db.request(request)
    filas_productos = db.cursor.fetchall()
    db.db_close()
    return filas_productos
    
# Funcion para eliminar un producto 
def eliminar_producto():
    db=ConexionDB("practico_evaluativo.db")
    request=f"delete from PRODUCTOS where cod_prod = {del_producto}"
    db.request()
    db.commit()
    db.db_close()