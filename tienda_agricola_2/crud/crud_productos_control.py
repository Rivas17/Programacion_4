from modelo.control_fertilizante import Control_fertilizante
from modelo.control_plagas import Control_plagas

class Crud_producto_fertilizante:
    producto_registrados = []

    def crear_producto_fertilizante(self,registro_ica,nombre_producto,frecuencia_aplicacion,
                        precio,fecha_ultima_aplicacion):
        producto = Control_fertilizante(registro_ica,nombre_producto,frecuencia_aplicacion
                                        ,precio,fecha_ultima_aplicacion)
        self.producto_registrados.append(producto)
        return producto

    def crear_producto_plagas(self,registro_ica,nombre_producto,frecuencia_aplicacion,
                        precio,periodo_carencia):
        producto = Control_plagas(registro_ica,nombre_producto,frecuencia_aplicacion
                                        ,precio,periodo_carencia)
        self.producto_registrados.append(producto)
        return producto


    def buscar_producto(self,registro):
        productos = []
        for p in self.producto_registrados:
            if p.registro_ica == registro:
                productos.append(p)
        return productos
            
    
    def eliminar_producto(self,registro):
        for p in self.producto_registrados:
            if p.registro_ica == registro:
                self.producto_registrados.remove(p)
                return True
        return False
    
    def listar_productos(self):
        return self.producto_registrados