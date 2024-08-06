from flask import render_template, make_response, request
from flask_restful import Resource
from models.heladeria import Heladeria
from models.venta import Venta
from models.productos import Productos



class ControllerVenta(Resource):

    def get(self):
        heladeria = Heladeria("La Heladeria")
        items = heladeria.lista_productos()
        return make_response(render_template("index.html", items=items))

    def post(self):
        producto_vender = None
        resultado_venta = ""
        valor_venta = 0

        try:
            id_producto = int(request.form['idProducto'].strip())
        except ValueError:
            resultado_venta = "Ooops! el ID:{0} de producto no existe.".format(request.form['idProducto'])
            venta = Venta(producto_vender, resultado_venta, valor_venta)
            return make_response(render_template("venta.html", venta=venta))

        print("id:", id_producto)
        heladeria = Heladeria("La Heladeria")

        lista_productos = heladeria.lista_productos()
        for producto in lista_productos:
            if producto.id == id_producto:
                producto_vender = producto
                print("nombre:", producto_vender.nombre)
                break
        if producto_vender is not None:
            try:
                resultado_venta = heladeria.vender(producto_vender.nombre)
                valor_venta = producto.precio_publico
            except ValueError as ex:
                resultado_venta = ex
        else:
            resultado_venta = "Ooops! el ID:{0} de producto no existe.".format(request.form['idProducto'])
            print(resultado_venta)

        venta = Venta(producto_vender, resultado_venta, valor_venta)
        return make_response(render_template("venta.html", venta=venta))