from conexion import ConexionDB

# Creacion de la base de datos
# Nombre de la base de datos: practico_evaluativo.db


conexionDB = ConexionDB("practico_evaluativo.db")
conexionDB.request("create table MARCAS (cod_marca int(10) not null primary key, descrip_marca varchar(50))")
conexionDB.request("create table PRODUCTOS (cod_prod int(10) not null primary key, descrip_prod varchar(50), cod_marca int(10), stock int, precio float, foreign key(cod_marca) references MARCAS(cod_marca))")
conexionDB.request("create table USUARIOS (cod_usuario int(10) not null primary key, username varchar(20), nombre_usur varchar(50), apellido_usur varchar(50), dni_usur varchar(9),password_usur varchar(20))")
conexionDB.db_close()