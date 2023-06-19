from conexion import ConexionDB
from modelo_producto import Producto

# Funcion para insertar un producto
def insertar_producto(cod_prod,descrip_prod,marca,stock,precio):
    producto=Producto(cod_prod,descrip_prod,marca,stock,precio)
    
    # Carga de productos en la base de datos
    db=ConexionDB("practico_evaluativo.db")
    request=f"insert into PRODUCTOS values({producto.cod_prod},'{producto.descrip_prod}','{producto.marca}',{producto.stock},{producto.precio})"
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
    
# Funcion para modificar un producto 
def modificar_producto(cod_prod,descrip_prod,marca,stock,precio):
    db=ConexionDB("practico_evaluativo.db")
    request=f"update PRODUCTOS set cod_prod = {cod_prod}, descrip_prod = '{descrip_prod}', marca = '{marca}', stock = {stock}, precio = {precio} where cod_prod = {cod_prod}"
    db.request(request)
    db.commit()
    db.db_close()    

# Funcion para eliminar un producto 
def eliminar_producto(cod_prod):
    db=ConexionDB("practico_evaluativo.db")
    request=f"delete from PRODUCTOS where cod_prod = {cod_prod}"
    db.request(request)
    db.commit()
    db.db_close()