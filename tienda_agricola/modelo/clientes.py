
class Cliente:
    def __init__(self,nombre,cedula):
        self._nombre = nombre
        self._cedula = cedula
        self._historial_pedidos = []
    
    def historial_pedidos(self):
        return self._historial_pedidos

    def agregar_pedido(self,pedido):
        self._historial_pedidos.append(pedido)

    def get_nombre(self):
        return self._nombre
    
    def get_cedula(self):
        return self._cedula

    def __str__(self):
        return f"Cliente: {self._nombre} - Cedula: {self._cedula}"
    