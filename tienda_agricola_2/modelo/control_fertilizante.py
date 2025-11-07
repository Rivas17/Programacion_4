from .productos_control import Productos_control

class Control_fertilizante(Productos_control):
    def __init__(self,registro_ica,nombre_producto,frecuencia_aplicacion,
                 precio,fecha_ultima_aplicacion):
        super().__init__(registro_ica,nombre_producto,frecuencia_aplicacion,precio)
        self.__ultima_aplicacion = fecha_ultima_aplicacion
    
    # def get_ultima_aplicacion(self):
    #     return self.__ultima_aplicacion

    def __str__(self):
        info = super().__str__() 
        return f"{info}Fecha de ultima aplicación: {self.__ultima_aplicacion}."
    
