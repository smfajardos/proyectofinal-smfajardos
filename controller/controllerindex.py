from flask import render_template, make_response
from flask_restful import Resource
from models.productos import Productos

class ControllerIndex(Resource):

    def get(self):
        producto = Productos("Heladería SF")
        items = producto.lista_productos()
        return make_response(render_template("index.html", items=items))