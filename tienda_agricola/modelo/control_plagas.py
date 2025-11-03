from .productos_control import Productos_control

class Control_plagas(Productos_control):
    def __init__(self,registro_ica,nombre_producto,frecuencia_aplicacion,
                 precio,periodo_carencia):
        super().__init__(registro_ica,nombre_producto,frecuencia_aplicacion,precio)
        self._periodo_carencia = periodo_carencia
    
    def get_periodo_carencia(self):
        return self._periodo_carencia

    def __str__(self):
        info = super().__str__() 
        return f"{info}Periodo de carencia: {self.perido_carencia} dias transcurridos."
    
