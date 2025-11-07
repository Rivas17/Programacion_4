import unittest
import sys
import os

# Agregar el directorio padre al path para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from crud.crud_clientes import Crud_cliente
from modelo.clientes import Cliente
from modelo.factura import Factura


class TestClientes(unittest.TestCase):

    def test_crear_cliente(self):
        crud = Crud_cliente()
        cliente1 = crud.crear_cliente("Juan", 12345)
        
        # Verificar que los atributos sean correctos
        self.assertIsInstance(cliente1, Cliente)
        self.assertEqual(cliente1.cedula,12345)
        self.assertEqual(len(cliente1.historial_pedidos), 0)

        cliente1 = crud.eliminar_cliente(12345)
        # print(cliente1)
        self.assertNotIsInstance(cliente1,Cliente)

    def test_obtener_cliente(self):
        crud = Crud_cliente()
        cliente1 = crud.crear_cliente("Camila", 67890)
        cliente2 = crud.obtener_cliente(67890)

        self.assertEqual(cliente1,cliente2)

    def test_listar_clientes(self):
        crud = Crud_cliente()
        cliente = crud.crear_cliente("Jorge",1234)
        lista = crud.listar_clientes()
        self.assertEqual(len(lista),1) 

    def test_eliminar_cliente(self):
        crud = Crud_cliente()
        cliente = crud.crear_cliente("David",1234)
        eliminado = crud.eliminar_cliente(1234)
        
        self.assertTrue(eliminado)


if __name__ == '__main__':
    unittest.main()