import models.funciones as Funciones
from models.productos import Productos
from models.ingredientes import Ingredientes
from db import db

class Heladeria:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__lista_productos = self.lista_productos()
        self.__venta_del_dia = 0

    def get_nombre(self) -> str:
        return self.__nombre

    def get_venta_del_dia(self) -> float:
        return self.__venta_del_dia

    def producto_mas_rentable(self) -> str:
        return Funciones.producto_mas_rentable(self.__lista_productos)

    def vender(self, nombre_producto: str) -> str:
        resultado = ""
        producto_vender = None
        msn_error = ""
        for producto in self.__lista_productos:
            if producto.nombre == nombre_producto:
                producto_vender = producto
                break
        if producto_vender is not None:
            lista_ingredientes = producto_vender.ingredientes
            ingredientes_completos = True
            lista_ingredientes_sin_inventario = []
            if len(lista_ingredientes) > 0:
                for ingrediente in lista_ingredientes:
                    "Validamos para cada ingrediente el inventario"
                    if ingrediente.ingrediente.sabor is not None and ingrediente.ingrediente.inventario < 1:
                        ingredientes_completos = False
                        lista_ingredientes_sin_inventario.append(ingrediente.ingrediente.nombre)
                    if ingrediente.ingrediente.sabor is None and ingrediente.ingrediente.inventario < 0.2:
                        ingredientes_completos = False
                        lista_ingredientes_sin_inventario.append(ingrediente.ingrediente.nombre)

                if ingredientes_completos:
                    "Como los ingredientes cumplen el inventario, entonces descontamos."
                    for ingrediente in lista_ingredientes:
                        "Descontamos del inventario"
                        if ingrediente.ingrediente.sabor is not None and ingrediente.ingrediente.inventario >= 1:
                            ingrediente.ingrediente.inventario = (ingrediente.ingrediente.inventario - 1)
                        if ingrediente.ingrediente.sabor is None and ingrediente.ingrediente.inventario >= 0.2:
                            ingrediente.ingrediente.inventario = (ingrediente.ingrediente.inventario - 0.2)
                    db.session.commit()
                    self.__venta_del_dia = self.__venta_del_dia + producto_vender.precio_publico
                    resultado = "¡Vendido!"
                else:
                    msn_error = "¡Oh no! Nos hemos quedado sin: {0}".format(lista_ingredientes_sin_inventario)
                    raise ValueError(msn_error)
            else:
                msn_error = "El producto no tiene ingredientes asignados."
                raise ValueError(msn_error)

        return resultado


    def lista_productos(self):
            productos = Productos.query.all()
            for item in productos:
                if item.vaso is None:
                    item.vaso = ""
                if item.volumen is None:
                    item.volumen = "0"
            return productos

    def lista_ingredientes(self):
        ingredientes = Ingredientes.query.all()
        for item in ingredientes:
            if item.es_vegetariano:
                item.es_vegetariano = "Si"
            else:
                item.es_vegetariano = "No"
            if item.sabor is None:
                item.sabor = ""
        return ingredientes
