from flask import render_template, make_response
from flask_restful import Resource
from models.productos import Productos


class ControllerProductos(Resource):
    
    def lista_productos(self):
        productos = Productos.query.all()
        return productos
    
