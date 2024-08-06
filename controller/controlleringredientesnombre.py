from flask import render_template, make_response
from flask_restful import Resource
from models.ingredientes import Ingredientes


class ControllerIngredientesNombre(Resource):
    
    def lista_ingredientes_nombre(self):
        ingredientes = Ingredientes.query.get(Ingredientes.nombre)
        return ingredientes
    