import os
from flask import Flask, request, render_template, redirect, url_for, session, abort
from flask_restful import Api
from flask_login import LoginManager, login_required, login_user, current_user
from dotenv import load_dotenv
from db import db
from controller.controllerindex import ControllerIndex
from controller.controllerheladeria import ControllerHeladeria
from controller.controllerproductos import ControllerProductos
from controller.controllerproductosid import ControllerProductosId
from controller.controllerproductosnombre import ControllerProductosNombre
from controller.controlleringredientes import ControllerIngredientes
from controller.controlleringredientesid import ControllerIngredientesId
from controller.controlleringredientesano import ControllerIngredienteSano
from controller.controlleringredientesnombre import ControllerIngredientesNombre
from controller.controllerproductosingredientes import ControllerProductosIngredientes
from controller.controllerproductoscalorias import ControllerProductosCalorias
from controller.controllerproductosrentabilidad import ControllerProductosRentabilidad
from controller.controllerproductoscosto import ControllerProductosCosto
from controller.controllerventa import ControllerVenta
from controller.controllerbienvenida import ControllerBienvenida
from models.heladeria import Heladeria
from models.user import Usuarios
from models.ingredientes import Ingredientes
from models.productos import Productos

load_dotenv()

secret_key = os.urandom(24)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:CGQqWBPPNhvOmphmEBaJUbZbAwyhBmvE@monorail.proxy.rlwy.net:10978/railway'
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    user = Usuarios.query.get(user_id)
    if user:
        return user
    return None

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        user = Usuarios.query.filter_by(username=username, password=password).first()
        if user:
            session ["usuario_nombre"] = user.username
            return redirect(url_for('bienvenida'))
        else:
            return "Credenciales inválidas", 401

@app.route ("/bienvenida")
def bienvenida():
    nombre = session.get("usuario_nombre", "Invitado")
    return render_template("bienvenida.html", nombre=nombre) 

@app.route("/index")
def index():
    nombre = session.get("usuario_nombre", "Invitado")
    return render_template("index.html", nombre=nombre) 

@app.route("/ingredientes")
def mostrar_ingredientes():
    if Usuarios.is_admin or Usuarios.is_empleado == True:
       ingredientes = Ingredientes.query.all()
       return render_template('ingredientes.html', ingredientes=ingredientes)
    else:
       return "No autorizado", 401

@app.route('/ingredientes/<int:id>')
def mostrar_ingredientes_id(id):
    if Usuarios.is_admin or Usuarios.is_empleado == True:
        ingredientes = Ingredientes.query.get(id)
        if ingredientes is None:
            abort(404) 
        return render_template('ingredientes_id.html', ingredientes=ingredientes)
    else:
        return "No autorizado", 401

@app.route('/ingrediente_sano/<int:id>')
def mostrar_ingredientes_sano(id):
    if Usuarios.is_admin or Usuarios.is_empleado == True:
        ingredientes = Ingredientes.query.get(id)
        if ingredientes is None:
            abort(404)
        if Ingredientes.es_vegetariano == 0:
            es_sano = "SI"
        else:
            es_sano = "NO"
        return render_template('ingrediente_sano.html', ingredientes=ingredientes, es_sano=es_sano)
    else:
        return "No autorizado", 401

@app.route('/ingredientes/<string:nombre>')
def mostrar_ingredientes_nombre(nombre):
    if Usuarios.is_admin or Usuarios.is_empleado == True:
        ingredientes = Ingredientes.query.filter_by(nombre=nombre).first()
        if ingredientes is None:
            abort(404) 
        return render_template('ingredientes_nombre.html', ingredientes=ingredientes)
    else:
        return "No autorizado", 401

@app.route('/productos')
def mostrar_productos():
    if Usuarios.is_admin or Usuarios.is_empleado == True:
        productos = Productos.query.all()
        return render_template('productos.html', productos=productos)
    else:
        return "No autorizado", 401

@app.route('/productos/<int:id>')
def mostrar_productos_id(id):
    if Usuarios.is_admin or Usuarios.is_empleado == True:
        productos = Productos.query.get(id)
        if productos is None:
            abort(404) 
        return render_template('productos_id.html', productos=productos)
    else:
        return "No autorizado", 401

@app.route('/productos/<string:nombre>')
def mostrar_productos_nombre(nombre):
    if Usuarios.is_admin or Usuarios.is_empleado == True:
        productos = Productos.query.filter_by(nombre=nombre).first()
        if productos is None:
            abort(404) 
        return render_template('productos_nombre.html', productos=productos)
    else:
        return "No autorizado", 401

@app.route('/calorias/<int:id>')
def consultar_calorias(id):
    if Usuarios.is_admin or Usuarios.is_empleado == True:
        calorias_ajustadas = 0
        producto = Productos.query.get(id)
        if producto is None:
            return "Producto no encontrado", 404
        total_calorias = sum(ingrediente.calorias for ingrediente in producto.ingredientes)
        if producto.id == 1:
            calorias_ajustadas = round(total_calorias * 0.95, 2)
        else:
            calorias_ajustadas = round(total_calorias, 2)
        return render_template('productos_calorias.html', producto=producto, calorias=calorias_ajustadas)
    else:
        return "No autorizado", 401


@app.route('/venta/<int:id>')
def venta(id):
    producto = Productos.query.get(id)
    if producto is None:
        return "Producto no encontrado", 404
    else:
        return render_template('venta.html', producto=producto, venta=venta)


@app.route('/rentabilidad/<int:id>')
def consultar_rentabilidad(id):
    if Usuarios.is_admin == True:
        rentabilidad = 0
        producto = Productos.query.get(id)
        if producto is None:
            return "Producto no encontrado", 404
        total_precio = sum(ingrediente.precio for ingrediente in producto.ingredientes)
        if producto.id == 1:
            rentabilidad = producto.precio_publico - total_precio
        else:
            rentabilidad = producto.precio_publico - (total_precio + 500)
        return render_template('productos_rentabilidad.html', producto=producto, rentabilidad=rentabilidad)
    else:
        return "No autorizado", 401


@app.route('/costo_produccion/<int:id>')
def costo_produccion(id):
    if Usuarios.is_admin == True:
        costo = 0
        producto = Productos.query.get(id)
        if producto is None:
            return "Producto no encontrado", 404
        costo = sum(ingrediente.precio for ingrediente in producto.ingredientes)
        if producto.id == 1:
            costo = costo
        else:
            costo = costo + 500
        return render_template('costo_produccion.html', producto=producto, costo=costo)
    else:
        return "No autorizado", 401


api.add_resource(ControllerIndex, '/index')
api.add_resource(ControllerHeladeria, '/heladeria')
api.add_resource(ControllerProductos, '/productos')
api.add_resource(ControllerProductosId, '/productos/<int:id>')
api.add_resource(ControllerProductosNombre, '/productos/<nombre>')
api.add_resource(ControllerProductosCalorias, '/calorias/<int:id>')
api.add_resource(ControllerProductosRentabilidad,'/rentabilidad/<int:id>')
api.add_resource(ControllerProductosCosto,'/costo_produccion/<int:id>')
api.add_resource(ControllerVenta,'/venta/<int:id>')
api.add_resource(ControllerIngredientes, '/ingredientes')
api.add_resource(ControllerIngredientesId, '/ingredientes/<int:id>')
api.add_resource(ControllerIngredienteSano, '/ingrediente_sano/<int:id>')
api.add_resource(ControllerIngredientesNombre, '/ingredientes/<nombre>')
api.add_resource(ControllerBienvenida, '/bienvenida')
api.add_resource(ControllerProductosIngredientes, '/productosingredientes')