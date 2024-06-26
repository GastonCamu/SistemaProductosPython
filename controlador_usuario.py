from conexion import ConexionDB
from modelo_usuario import Usuario

# Funcion para crear un usuario
def crear_usuario(username,nombre_usur,apellido_usur,dni_usur,password_usur):
    usuario=Usuario(username,nombre_usur,apellido_usur,dni_usur,password_usur)
    
    # Carga de usuario en la base de datos
    db=ConexionDB("practico_evaluativo.db")
    request=f"insert into USUARIOS ('username','nombre_usur','apellido_usur','dni_usur','password_usur') values('{usuario.username}','{usuario.nombre_usur}','{usuario.apellido_usur}',{usuario.dni_usur},'{usuario.password_usur}')"
    db.request(request)
    db.commit()
    db.db_close()
    
# Funcion para verificar el usuario y contraseña en la base de datos
def verificar_usuario(username,password):
    db = ConexionDB("practico_evaluativo.db")
    request = f"SELECT password_usur FROM USUARIOS WHERE username = '{username}'"
    db.request(request)
    original = db.cursor.fetchone()
    if original == None:
        return False
    else:
        for fila in original:
            original_pass = fila
        if original_pass == password:
            return True
        else:
            return False