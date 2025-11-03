class Productos_control:
    def __init__(self,registro_ica, nombre_producto,frecuencia_aplicacion,precio):
        self._registro_ica = registro_ica
        self._nombre = nombre_producto
        self._frecuencia_aplicacion = frecuencia_aplicacion
        self._precio = precio

    def get_nombre(self):
        return self._nombre
    
    def get_precio(self):
        return self._precio

    def __str__(self):
        return f"""Registro ICA: {self._registro_ica} -- Nombre producto: {self._nombre}
                \nFrecuencia aplicacion: {self._frecuencia_aplicacion} -- Valor: {self._precio}\n"""
    
