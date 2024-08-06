from flask_login import UserMixin
from db import db

class Usuarios(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    is_empleado = db.Column(db.Boolean, nullable=False)
    is_cliente = db.Column(db.Boolean, nullable=False)
    
    
    def __init__(self, id, username, password, is_admin, is_empleado, is_cliente):
        self.id = id
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.is_empleado = is_empleado
        self.is_cliente = is_cliente

    def lista_usuarios(self):
        user = Usuarios.query.all()
        return user
    
