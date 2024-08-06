from models.productos import Productos



class Venta:
    def __init__(self, producto: Productos, resultado: str, valor: float):
        self.producto = producto
        self.resultado = resultado
        self.valor = valor
