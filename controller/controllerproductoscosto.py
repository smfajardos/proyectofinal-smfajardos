from flask import render_template, make_response
from flask_restful import Resource
from models.heladeria import Heladeria


class ControllerProductosCosto(Resource):

    def get(self):
        heladeria = Heladeria("La Heladeria")
        items = heladeria.lista_productos()
        return make_response(render_template("productos.html", items=items))