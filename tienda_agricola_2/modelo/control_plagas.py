from .productos_control import Productos_control

class Control_plagas(Productos_control):
    def __init__(self,registro_ica,nombre_producto,frecuencia_aplicacion,
                 precio,periodo_carencia):
        super().__init__(registro_ica,nombre_producto,frecuencia_aplicacion,precio)
        self.__periodo_carencia = periodo_carencia
    
    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    def __str__(self):
        info = super().__str__() 
        return f"{info}Periodo de carencia: {self.__perido_carencia} dias transcurridos."
    
