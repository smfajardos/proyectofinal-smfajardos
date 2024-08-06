from flask import render_template, make_response
from flask_restful import Resource
from models.heladeria import Heladeria

class ControllerIngredienteSano(Resource):

    def get(self):
        heladeria = Heladeria("La Heladeria")
        ingredientes = heladeria.lista_ingredientes()
        return make_response(render_template("ingrediente_sano.html", ingredientes=ingredientes))