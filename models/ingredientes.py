from db import db

class Ingredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    calorias = db.Column(db.Integer(), nullable=False)
    es_vegetariano = db.Column(db.Boolean(), nullable=False)
    inventario = db.Column(db.Integer(), nullable=False)
    sabor = db.Column(db.String(45), nullable=True)

    def __init__(self, nombre: str, precio: float, calorias: int, es_vegetariano: bool, inventario: float, sabor: str):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self.es_vegetariano = es_vegetariano
        self.inventario = inventario
        self.sabor = sabor

    def lista_ingredientes(self):
        ingredientes = Ingredientes.query.all()
        return ingredientes
    
    