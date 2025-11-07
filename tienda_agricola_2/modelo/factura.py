from datetime import datetime
from .clientes import Cliente
from  .productos_control import Productos_control
from .antibioticos import Antibiotico

class Factura:
    def __init__(self, cliente):
        if not isinstance(cliente, Cliente):
            print("Datos del cliente inválidos.")
            return
        
        self.__cliente = cliente
        self.__productos = {}
        self.__fecha = datetime.now()
        self.__valor_total = 0
        
        cliente.agregar_pedido(self)

    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def productos(self):
        return self.__productos
    
    @property
    def valor_total(self):
        return self.__valor_total
    
    @property
    def fecha(self):
        return self.__fecha

    def agregar_producto(self, producto,cantidad):
        if not isinstance(producto, (Productos_control,Antibiotico)):
            print("El producto ingresado es inválido.")
            return
        
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
        
        if producto not in self.__productos:
            self.__productos[producto] = cantidad
        else:
            self.__productos[producto] += cantidad

        self.calcular_total()

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.__productos.items():
            total += producto.precio * cantidad
            
        self.__valor_total = total

   
    
