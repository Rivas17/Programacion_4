import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modelo.clientes import Cliente
from modelo.control_plagas import Control_plagas
from modelo.antibioticos import Antibiotico
from modelo.factura import Factura

class TestFacturas(unittest.TestCase):
    
    def test_crear_factura(self):
        """Test creación básica de factura"""
        cliente = Cliente("Carlos", "11223344")
        factura = Factura(cliente)
        
        self.assertEqual(factura.get_cliente(), cliente)
        self.assertEqual(factura.get_valor_total(), 0)
        self.assertEqual(len(factura.get_productos()), 0)
    
    def test_factura_agregar_productos(self):
        """Test agregar productos y calcular total"""
        cliente = Cliente("Ana", "5678")
        factura = Factura(cliente)
        
        # Crear productos de prueba
        plaguicida = Control_plagas("ICA-001", "Plaguicida X", "Cada 15 dias", 40000, 25)
        antibiotico = Antibiotico("Antibiotico K", 35000, 500, "Porcinos")
        
        # Agregar productos a la factura
        factura.agregar_producto(plaguicida, 2)  # 2 x 40000 = 80000
        factura.agregar_producto(antibiotico, 1) # 1 x 35000 = 35000
                                                # TOTAL = 115000
        
        self.assertEqual(len(factura.get_productos()), 2)
        self.assertEqual(factura.get_valor_total(), 115000)
    
    
if __name__ == '__main__':
    unittest.main()