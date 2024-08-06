from flask import render_template, make_response
from flask_restful import Resource
from models.productosingredientes import ProductosIngredientes


class ControllerProductosIngredientes(Resource):

    def get(self):
        items = ProductosIngredientes.query.all()
        return make_response(render_template("productosingredientes.html", items=items))