import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modelo.control_plagas import Control_plagas
from modelo.control_fertilizante import Control_fertilizante
from modelo.antibioticos import Antibiotico

class TestProductos(unittest.TestCase):
    
    def test_crear_control_plagas(self):
        """Test creación de control de plagas"""
        producto = Control_plagas("ICA-001","Plaguicida A","Cada 15 días",50000,20)
        
        self.assertEqual(producto.get_nombre(), "Plaguicida A")
        self.assertEqual(producto.get_periodo_carencia(), 20)
        self.assertEqual(producto.get_precio(), 50000)
    
    def test_crear_antibiotico(self):
        """Test creación de antibiótico con datos válidos
            Dosis:entre 400-600"""
        antibiotico = Antibiotico("Antibiótico B",30000,450,"Bovinos")
        
        self.assertEqual(antibiotico.get_dosis(), 450)
        self.assertEqual(antibiotico.get_tipo_animal(), "Bovinos")
    

if __name__ == '__main__':
    unittest.main()