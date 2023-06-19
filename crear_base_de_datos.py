from conexion import ConexionDB

# Creacion de la base de datos
# Nombre de la base de datos: practico_evaluativo.db


conexionDB = ConexionDB("practico_evaluativo.db")
conexionDB.request("create table PRODUCTOS (cod_prod int(10) not null primary key, descrip_prod varchar(50), marca varchar(15), stock int, precio float)")
conexionDB.request("create table USUARIOS (cod_usuario integer primary key autoincrement, username varchar(20), nombre_usur varchar(50), apellido_usur varchar(50), dni_usur varchar(9),password_usur varchar(20))")
conexionDB.db_close()