from flask import render_template, make_response
from flask_restful import Resource
from models.productos import Productos


class ControllerProductosCalorias(Resource):
    
    def lista_productos_calorias(self):
        productos = Productos.query.get(Productos.id)
        return productos
    