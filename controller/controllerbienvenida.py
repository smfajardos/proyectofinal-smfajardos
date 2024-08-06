from flask import render_template, make_response
from flask_restful import Resource
from models.user import Usuarios


class ControllerBienvenida(Resource):

    def get(self):
        items = Usuarios.query.all()
        return make_response(render_template("bienvenida.html", items=items))