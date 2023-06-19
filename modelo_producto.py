# Creacion de la clase producto

class Producto():
    def __init__(self,cod_prod, descrip_prod, marca, stock, precio):
        self.cod_prod = cod_prod
        self.descrip_prod = descrip_prod
        self.marca = marca
        self.stock = stock
        self.precio = precio