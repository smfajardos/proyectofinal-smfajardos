from db import db
import models.funciones as Funciones
import models.ingredientes as Ingredientes
import models.productosingredientes as ProductosIngredientes
from flask import Flask, request, render_template, redirect, url_for, session, abort


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio_publico = db.Column(db.Float(), nullable=False)
    vaso = db.Column(db.String(), nullable=True)
    volumen = db.Column(db.Integer(), nullable=True)
    ingredientes = db.relationship('Ingredientes', secondary='productos_ingredientes',  backref='productos')
    
    def __init__(self, nombre:str, precio_publico:float, vaso:str, volumen:str, ingredientes:list):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.vaso = vaso
        self.volumen = volumen
        self.ingredientes = ingredientes

    def calcular_calorias(self) -> float:
        lista_calorias = []
        for ingredientes in ingredientes:
            lista_calorias.append(ingredientes)
        if Productos.id == 2:
            return Funciones.contar_calorias_malteada(lista_calorias) + 200
        else:
            return Funciones.contar_calorias_copa(lista_calorias)

        

