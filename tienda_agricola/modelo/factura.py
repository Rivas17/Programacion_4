from datetime import datetime
from .clientes import Cliente
from  .productos_control import Productos_control
from .antibioticos import Antibiotico

class Factura:
    def __init__(self, cliente):
        if not isinstance(cliente, Cliente):
            print("Datos del cliente inválidos.")
            return
        
        self._cliente = cliente
        self._productos = {}
        self._fecha = datetime.now()
        self._valor_total = 0
        
        cliente.agregar_pedido(self)

    def agregar_producto(self, producto,cantidad):
        if not isinstance(producto, (Productos_control,Antibiotico)):
            print("El producto ingresado es inválido.")
            return
        
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
        
        if producto not in self._productos:
            self._productos[producto] = cantidad
        else:
            self._productos[producto] += cantidad

        self.calcular_total()

    def calcular_total(self):
        total = 0
        for producto, cantidad in self._productos.items():
            total += producto.get_precio() * cantidad
            
        self._valor_total = total

    def get_cliente(self):
        return self._cliente
    
    def get_productos(self):
        return self._productos
    
    def get_valor_total(self):
        return self._valor_total
    
    def get_mostrar_fecha(self):
        return self._fecha
    
