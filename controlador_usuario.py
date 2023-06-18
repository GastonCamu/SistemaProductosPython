from conexion import ConexionDB
from modelo_usuario import Usuario

# Funcion para crear un usuario
def crear_usuario():
    
    # Ingreso de datos por el usuario.
    
    cod_usuario=int(input("Ingrese el código del nuevo usuario: "))
    username=input("Ingrese el nombre con el cuál ingresará al sistema: ")
    nombre_usur=input("Ingrese el nombre: ")
    apellido_usur=input("Ingrese el apellido: ")
    dni_usur=input("Ingrese el número de DNI: ")
    password_usur=input("Ingrese la contraseña: ")
    usuario=Usuario(cod_usuario,username,nombre_usur,apellido_usur,dni_usur,password_usur)
    
    # Carga de usuario en la base de datos
    
    db=ConexionDB("practico_evaluativo.db")
    request=f"insert into USUARIOS values({usuario.cod_usuario},'{usuario.username}','{usuario.nombre_usur}','{usuario.apellido_usur}',{usuario.dni_usur},'{usuario.password_usur}')"
    db.request(request)
    db.commit()
    db.db_close()

# Funcion para eliminar a un usuario
def eliminar_usuario():
    db=ConexionDB("practico_evaluativo.db")
    request = f"delete from USUARIOS where dni_usur ='{del_usuario}'"
    db.request(request)
    db.commit()
    db.db_close()

# Funcion para verificar el usuario y contraseña en la base de datos
def verificar_usuario(username, password):
    db = ConexionDB("practico_evaluativo.db")
    request = f"SELECT * FROM USUARIOS WHERE username = '{username}' AND password_usur = '{password}'"
    db.request(request)
    pass_original = db.cursor.fetchone()
    db.db_close()
