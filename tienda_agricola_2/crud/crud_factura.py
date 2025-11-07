from modelo.factura import Factura
from modelo.clientes import Cliente

class Crud_Factura:
    factura_registradas = []

    def crear_factura(self,cliente,lista_productos):
        factura = Factura(cliente)

        for producto,cantidad in lista_productos:
            factura.agregar_producto(producto,cantidad)
        
        self.factura_registradas.append(factura)
        return factura
    
    def mostrar_facturas(self):
        return self.factura_registradas

    def buscar_facturas_cliente(self,cedula):
        facturas_cliente = []
        for factura in self.factura_registradas:
            if factura.cliente.cedula == cedula:
                facturas_cliente.append(factura)
        return facturas_cliente
    
    def eliminar_facturas(self, cliente):
        original = len(self.factura_registradas)
        self.factura_registradas = [
            f for f in self.factura_registradas if f.cliente != cliente 
            ]
        return len(self.factura_registradas) < original
