
from Model.hospital import Hospital 
from Model.doctor import Doctor

class HospitalController:
    def __init__(self):
        self.hospital = None # Almacenará el único objeto Hospital
        self.bloquear_campo_hospital = False

    def crear_hospital(self, nombre):
        if self.hospital is None:
            self.hospital = Hospital(nombre)
            return f"Hospital '{nombre}' creado."
        else:
            if self.bloquear_campo_hospital:
                return f"Hospital bloqueado '{self.hospital.nombre_hospital}'(no se puede cambiar)."
            # else:
            #     # Si ya existe, simplemente podrías actualizar el nombre si fuera necesario.
            #     self.hospital.hospital_name = hospital_name
            #     return f"Hospital actualizado a '{hospital_name}'."
    
    def bloquear_hospital(self):
        self.bloquear_campo_hospital = True

    def verificar_dni(self, dni):
        if self.hospital is None:
            return False # No hay hospital, no puede existir el DNI

        for doctor in self.hospital.lista_doctores: 
            if doctor.dni == dni:
                return True 
        return False

    def almacenar_doctor(self, dni,nombre_doctor, especialidad):

        if self.hospital is None:
            return "Error: El hospital aún no ha sido creado."

        if self.verificar_dni(dni):
            return f"Error: Ya existe un doctor registrado con el DNI: {dni}"

        nuevo_doctor = Doctor(dni,nombre_doctor,especialidad)
        self.hospital.añadir_doctor(nuevo_doctor)
        
        if not self.bloquear_campo_hospital:
            self.bloquear_campo_hospital = True

        return f"Doctor '{nombre_doctor}' creado y asociado a '{self.hospital.nombre_hospital}'."

    def buscar_dni(self, dni):
        if self.hospital is None:
            return [] 

        for doctor in self.hospital.lista_doctores:
            if doctor.dni == dni:
                return [
                    {
                        'dni': doctor.dni,
                        'nombre': doctor.nombre,
                        'especialidad': doctor.especialidad,
                        'nombre_hospital': self.hospital.nombre_hospital
                    }
                ]
        
        return []