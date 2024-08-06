from flask import render_template, make_response
from flask_restful import Resource
from models.productos import Productos


class ControllerProductosRentabilidad(Resource):
    
    def lista_productos_rentabilidad(self):
        productos = Productos.query.get(Productos.id)
        return productos
    