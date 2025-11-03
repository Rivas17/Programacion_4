import unittest
import sys
import os

# Agregar el directorio padre al path para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modelo.clientes import Cliente
from modelo.factura import Factura

class TestClientes(unittest.TestCase):
    
    def test_crear_cliente(self):
        """Test que verifica la creación correcta de un cliente"""
        cliente = Cliente("Juan", "12345678")
        
        # Verificar que los atributos sean correctos
        self.assertEqual(cliente.get_nombre(), "Juan")
        self.assertEqual(cliente.get_cedula(), "12345678")
        self.assertEqual(len(cliente.historial_pedidos()), 0)
    
    def test_cliente_agregar_factura(self):
        """Test que verifica que se pueden agregar facturas al historial"""
        cliente = Cliente("Camila", "87654321")
        factura = Factura(cliente)
        
        # Verificar que la factura se agregó al historial
        self.assertEqual(len(cliente.historial_pedidos()), 1)
        self.assertIn(factura,cliente.historial_pedidos())

if __name__ == '__main__':
    unittest.main()