from modelo.antibioticos import Antibiotico

class CrudAntibiotico:
    producto_registrados = []

    def crear_antibiotico(self, nombre, precio,dosis,tipo_animal):
        producto = Antibiotico(nombre,precio,dosis,tipo_animal)
        self.producto_registrados.append(producto)
        return producto

    def buscar_producto(self,nombre):
        return [p for p in self.producto_registo if p.nombre == nombre]
    
    def eliminar_producto(self,nombre):
        for p in self.producto_registrados:
            if p.nombre == nombre:
                self.producto_registrados.remove(p)
                return True
        return None
    
    def listar_productos(self):
        return self.producto_registrados