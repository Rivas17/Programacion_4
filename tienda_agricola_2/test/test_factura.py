import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from crud.crud_factura import Crud_Factura
from crud.crud_clientes import Crud_cliente
from modelo.factura import Factura
from modelo.antibioticos import Antibiotico

class TestFacturas(unittest.TestCase):
    
    def setUp(self):
        self.crud_cliente = Crud_cliente()
        self.crud_factura = Crud_Factura()
        self.producto = Antibiotico("Amoxicilina",150,500,"Porcinos")


    def test_crear_factura(self):
        cliente = self.crud_cliente.crear_cliente("David",1234)
        lista_productos = [(self.producto, 3)]
        factura = self.crud_factura.crear_factura(cliente,lista_productos)

        self.assertIsNotNone(factura)
        self.assertEqual(factura.cliente, cliente)
        self.assertEqual(len(factura.productos), 1)
        self.assertEqual(factura.valor_total, self.producto.precio * 3)


    def test_buscar_facturas_por_cliente(self):
        cliente = self.crud_cliente.crear_cliente("David",1234)
        lista_productos = [(self.producto, 1)]
        self.crud_factura.crear_factura(cliente, lista_productos)

        resultado = self.crud_factura.buscar_facturas_cliente(1234)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].cliente.cedula, 1234)

    def test_eliminar_todas_facturas_de_cliente(self): 
        lista_productos = [(self.producto, 1)]
        cliente = self.crud_cliente.crear_cliente("Pablo",789)

        # Dos facturas del mismo cliente
        self.crud_factura.crear_factura(cliente, lista_productos)
        self.crud_factura.crear_factura(cliente, lista_productos)

        # Se crea otro cliente
        cliente2 = self.crud_cliente.crear_cliente("Carlos", 456)
        self.crud_factura.crear_factura(cliente2, lista_productos)

        # Verificar que están las facturas
        self.assertEqual(len(self.crud_factura.mostrar_facturas()), 5)
        
        eliminadas = self.crud_factura.eliminar_facturas(cliente)
        self.assertTrue(eliminadas)
        
        restantes = self.crud_factura.mostrar_facturas()
        # self.assertEqual(len(restantes), 1)
        self.assertEqual(restantes[0].cliente.nombre, "Carlos" and "David")

    
    
if __name__ == '__main__':
    unittest.main()