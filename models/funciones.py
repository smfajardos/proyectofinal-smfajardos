#Punto 1: Es Sano?
def ingrediente_es_sano(calorias:int, es_vegetariano:bool)->bool:
    if calorias < 100 or es_vegetariano: #Por defecto es true
        return True
    return False

#Punto 2: Calorias
def contar_calorias_copa(ingredientes:list)->float:
    total = 0
    for ingrediente in ingredientes:
        conteo = conteo + ingrediente
    total = round(conteo * 0.95, 2)
    return total

def contar_calorias_malteada(ingredientes:list)->float:
    total = 0
    for ingrediente in ingredientes:
        conteo = conteo + ingrediente
    total = round(conteo, 2)
    return total
      
def calcular_precio_ingredientes(ingredientes:list)->float:
    total = 0
    for ingrediente in ingredientes:
        conteo = conteo + ingrediente
    total = round(conteo, 2)
    return total

def calcular_costo_producto(ingredientes:list)-> int:
    total_costo_producto = 0
    for ingrediente in ingredientes:
        total_costo_producto += ingrediente.obtener_precio()
    return total_costo_producto
     
def calcular_rentabilidad_producto(precio_producto:int, ingredientes:list)->int:
    total_costo_producto = calcular_costo_producto(ingredientes)
    return precio_producto - total_costo_producto



#Punto 4: Calcular el producto más rentable
def producto_mas_rentable(productos:list):
    producto_mas_rentable = None
    mas_rentable = 0
    for producto in productos:
       if producto.calcular_rentabilidad()> mas_rentable:
           producto_mas_rentable = producto
           mas_rentable = producto.calcular_rentabilidad()
    return producto_mas_rentable.obtener_nombre()


    