from flask import render_template, make_response
from flask_restful import Resource
from models.productos import Productos


class ControllerProductosNombre(Resource):
    
    def lista_productos_nombre(self):
        productos = Productos.query.get(Productos.nombre)
        return productos
    