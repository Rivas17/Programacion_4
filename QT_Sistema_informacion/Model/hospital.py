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

#Ejemplo de uso (esto no va en el archivo, es solo para entender):
# mi_hospital = Hospital("Hospital Central")
# doc = Doctor(123,"David","Cirujano de rodilla")
# mi_hospital.añadir_doctor("jorge")
# mi_hospital.añadir_doctor(doc)
# print(mi_hospital)
# print(doc.informacion())
