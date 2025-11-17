import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))


from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox
from Controller.controller import HospitalController 

class HospitalApp(QMainWindow):
    def __init__(self):
        super().__init__()

        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, 'QT','hospital_main.ui')

        uic.loadUi(ruta_ui, self) #Cargar el diseño ui
        self.controller = HospitalController()
        self.pushButton_crear.clicked.connect(self.crear_nuevo_doctor)
        self.pushButton_buscar.clicked.connect(self.buscar_dni)
        self.tabla_grid()
        self.setFixedSize(self.size())
        self.show() # Muestra la ventana
        
    def tabla_grid(self):
        self.tableWidget_resultados.setColumnCount(4)
        self.tableWidget_resultados.setHorizontalHeaderLabels([
            "DNI Doctor", 
            "Nombre Doctor", 
            "Especialidad", 
            "Nombre Hospital"
        ])
    
    def crear_nuevo_doctor(self):
        #Datos de los Line Edits
        dni = self.lineEdit_dni_doctor.text().strip()
        nombre = self.lineEdit_nombre_doctor.text().strip()
        especialidad = self.lineEdit_especialidad.text().strip()
        
        if self.controller.hospital is None:
            nombre_hospital = self.lineEdit_nombre_hospital.text().strip()
            if not nombre_hospital:
                QMessageBox.warning(self, "Error", "Debe ingresar el nombre del hospital antes de crear el primer doctor.")
                return
            msg = self.controller.crear_hospital(nombre_hospital)
            print(msg)
        
        mensaje = self.controller.almacenar_doctor(dni,nombre, especialidad)
        
        if mensaje.startswith("Error:"):
            QMessageBox.warning(self, "Error de Registro", mensaje)
        else:
            QMessageBox.information(self, "Registro Exitoso", mensaje)
            
            self.lineEdit_dni_doctor.clear()
            self.lineEdit_nombre_doctor.clear()
            self.lineEdit_especialidad.clear()
        
        # Si el hospital quedó bloqueado tras el primer doctor, deshabilitar y cambiar color
        if self.controller.bloquear_campo_hospital and not self.lineEdit_nombre_hospital.isReadOnly():
            self.entrada_nombre_hospital()

    def entrada_nombre_hospital(self):
        self.lineEdit_nombre_hospital.setReadOnly(True)
        self.lineEdit_nombre_hospital.setStyleSheet(
            "QLineEdit { background-color: #D3D3D3; color: #666666; }"
        )

    def buscar_dni(self):
        encontrar_dni = self.lineEdit_dni_busqueda.text().strip()
        
        if not encontrar_dni:
            QMessageBox.warning(self, "Error", "Debe ingresar un DNI para buscar.")
            return
        
        resultado = self.controller.buscar_dni(encontrar_dni)
        
        self.tableWidget_resultados.setRowCount(0) #Limpia la tabla anterior
        
        if resultado:
            # 3. Insertar el resultado en el Table Widget
            data = resultado[0]
            posicion_fila = self.tableWidget_resultados.rowCount()
            self.tableWidget_resultados.insertRow(posicion_fila)
            self.tableWidget_resultados.setItem(posicion_fila, 0, QTableWidgetItem(data['dni']))
            self.tableWidget_resultados.setItem(posicion_fila, 1, QTableWidgetItem(data['nombre']))
            self.tableWidget_resultados.setItem(posicion_fila, 2, QTableWidgetItem(data['especialidad']))
            self.tableWidget_resultados.setItem(posicion_fila, 3, QTableWidgetItem(data['nombre_hospital']))
    
            QMessageBox.information(self, "Busqueda Exitosa", f"Doctor con DNI {encontrar_dni} encontrado.")
        else:
            QMessageBox.warning(self, "Doctor NO encontrado!", f"No se encontró un doctor con DNI: {encontrar_dni}")
            self.lineEdit_dni_busqueda.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HospitalApp()
    sys.exit(app.exec_())