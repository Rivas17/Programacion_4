from .doctor import Doctor

class Hospital:
    def __init__(self, nombre):
        self.nombre_hospital = nombre
        self.lista_doctores = []

    def añadir_doctor(self, doctor):
        if isinstance(doctor,Doctor):
            self.lista_doctores.append(doctor)

    def informacion(self):
        return {
            'nombre_hospital': self.nombre_hospital
        }

    def __str__(self):
        return f"Hospital: {self.nombre_hospital} ({len(self.lista_doctores)} Doctores)"
