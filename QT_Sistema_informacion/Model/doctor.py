class Doctor:
    def __init__(self,dni,nombre,especialidad):
        self.__dni = dni
        self.__nombre = nombre
        self.__especialidad = especialidad

    @property
    def dni(self):
        return self.__dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def especialidad(self):
        return self.__especialidad
    
    def informacion(self):
        return {
            'DNI': self.__dni,
            'Nombre': self.__nombre,
            'Especialidad': self.__especialidad
        }