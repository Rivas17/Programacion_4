
class Cliente:
    def __init__(self,nombre,cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__historial_pedidos = []
    
    @property
    def historial_pedidos(self):
        return self.__historial_pedidos

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cedula(self):
        return self.__cedula
    
    def agregar_pedido(self,pedido):
        self.__historial_pedidos.append(pedido)

    def __str__(self):
        return f"Cliente: {self.__nombre} - Cedula: {self.__cedula}"
    