class Productos_control:
    def __init__(self,registro_ica, nombre_producto,frecuencia_aplicacion,precio):
        self.__registro_ica = registro_ica
        self.__nombre = nombre_producto
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio

    def __str__(self):
        return f"""Registro ICA: {self.__registro_ica} -- Nombre producto: {self.__nombre}
                \nFrecuencia aplicacion: {self.__frecuencia_aplicacion} -- Valor: {self.__precio}\n"""
    
