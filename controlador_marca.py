from conexion import ConexionDB
from modelo_marcas import Marcas

# Funcion para insertar una marca
def insertar_marca():
    cod_marca=int(input("Ingrese el código de la marca: "))
    descrip_marca=input("Descripción: ")
    marca=Marcas(cod_marca,descrip_marca)
    db=ConexionDB("practico_evaluativo.db")
    request=f"insert into MARCAS values({marca.cod_marca},'{marca.descrip_marca}')"
    db.request(request)
    db.commit()
    db.db_close()

# Funcion para borrar una marca
def eliminar_marca():
    db=ConexionDB("practico_evaluativo.db")
    request = f"delete from MARCAS where cod_marca ='{del_marca}'"
    db.request(request)
    db.commit()
    db.db_close()
    
# Funcion para consultar marcas
def consultar_marcas():
    db=ConexionDB("practico_evaluativo.db")
    request=f"select * from MARCAS"
    db.request(request)
    filas_marcas=db.cursor.fetchall()
    print("Tabla MARCAS:")
    print("Cód. Marca // Descripción")
    for fila in filas_marcas:
        print(f"{fila[0]}          //   {fila[1]}")
    db.db_close()
