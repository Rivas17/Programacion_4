from modelo.clientes import Cliente

class Crud_cliente:
    clientes_registrados = []

    def crear_cliente(self,nombre,cedula):
        cliente = Cliente(nombre,cedula)
        self.clientes_registrados.append(cliente)
        return cliente

    def eliminar_cliente(self,cedula):
        
        for c in self.clientes_registrados:
            if c.cedula == cedula:
                self.clientes_registrados.remove(c)
                return True  
        return None
        
    def actualizar_nombre(self,cedula,nombre_nuevo):
        for c in self.clientes_registrados:
            if cedula == c.cedula:
                c.nombre = nombre_nuevo
                return True
        return None

    def obtener_cliente(self,cedula):
        for c in self.clientes_registrados:
            if c.cedula == cedula:
                return c
        return None

    def listar_clientes(self):
        return self.clientes_registrados
