from flask import render_template, make_response
from flask_restful import Resource
from models.heladeria import Heladeria

class ControllerIngredientesId(Resource):

    def get(self):
        heladeria = Heladeria("La Heladeria")
        ingredientes = heladeria.lista_ingredientes()
        return make_response(render_template("ingredientes.html", ingredientes=ingredientes))