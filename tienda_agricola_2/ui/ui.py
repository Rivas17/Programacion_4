from modelo.clientes import Cliente
from modelo.antibioticos import Antibiotico
from modelo.control_fertilizante import Control_fertilizante
from modelo.control_plagas import Control_plagas
from modelo.factura import Factura

class MenuPrincipal:
    def __init__(self):
        self.clientes = []
        self.productos = []
        self.facturass = []

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = int(input("Seleccione una opcion: "))
            print("\n")

            match opcion:
                case 1:
                    self.crear_producto_control()
                case 2:
                    self.crear_antibiotico()
                case 3:
                    self.crear_factura()
                case 4:
                    self.mostrar_cliente()
                case 5:
                    self.mostrar_facturas()
                case 0:
                    break
                case _:
                    print("Opcion incorrecta.")

    def mostrar_menu(self):
        print("\n\t-> Menu principal <-")
        print("1. Crear producto de control.")
        print("2. Crear Antibiotico.")
        print("3. Crear factura.")
        print("4. Mostrar clientes.")
        print("5. Mostrar facturas.")
        print("0. Salir")


    def crear_producto_control(self):
        print("Escoja una de las dos opciones:\n1. Control de plagas.\n2.Control de fertilizantes.")
        tipo = int(input("Opcion: "))

        if (tipo > 2 or tipo < 1):
            print("Numero invalido.")
            return

        registro_ica = input("Registro ICA: ")
        nombre = input("Nombre del producto: ")
        frecuencia = input("Frecuencia de aplicación: ")
        precio = float(input("Precio: "))

        if tipo == 1:
            periodo_carencia = int(input("Periodo de carencia (dias): "))
            producto = Control_plagas(registro_ica,nombre,frecuencia,precio,periodo_carencia)
        else:
            ultima_fecha = input("Ultima fecha de aplicacion (Año-Mes-Dia): ")
            producto = Control_fertilizante(registro_ica,nombre,frecuencia,precio,ultima_fecha)
        
        self.productos.append(producto)
        print("¡Producto Creado!")

    def crear_antibiotico(self):
        nombre = input("Ingrese el nombre: ")
        precio = float(input("Ingrese el precio: "))
        dosis = float(input("Ingrese la dosis (400-600)Kg: "))
        tipo_animal = input("Ingrese el tipo de animal(Bovinos, Porcionos, Caprinos): ").capitalize()

        try:
            antibiotico = Antibiotico(nombre,precio,dosis,tipo_animal)
        except ValueError as e:
            print(f"No se creo el producto: {e}")
            return
        
        self.productos.append(antibiotico)
        print("¡Producto Creado!")
    
    def crear_factura(self):
        
        if not self.productos:
            print("No se encuentra ningun producto registrado.")
            return
        
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cedula: ")
        cliente = self.crear_cliente(nombre,cedula)

        factura = Factura(cliente)
        while True:
            print(f"\nProductos disponibles:")
            for contador,producto in enumerate(self.productos):
                print(f"{contador+1}. {producto.nombre}")
            
            print("0. Para finalizar.")
            
            id_producto = int(input("Seleccione producto (numero - indice): ")) - 1
            
            if id_producto < 0: 
                break

            producto = self.productos[id_producto]
            cantidad = int(input("Ingrese la cantidad: "))
            factura.agregar_producto(producto,cantidad)
            print(f"Total actual: {factura.valor_total}")
            
        if factura.valor_total > 0:
            self.facturass.append(factura)
            print("Factura creada!.")
            
    
    def crear_cliente(self,nombre,cedula):
        
        for c in self.clientes:
            if c.cedula == cedula:
                return c

        cliente = Cliente(nombre, cedula)
        self.clientes.append(cliente)
        print("Cliente creado.")
        return cliente
    
    def mostrar_cliente(self):
        print("\nCLIENTES REGISTRADOS.")
        for cliente in self.clientes:
            print(f"Nombre: {cliente.nombre} - Cedula: {cliente.cedula}")
            print(f"Facturas: {len(cliente.historial_pedidos)}\n")
    
    def mostrar_facturas(self):
        print("\nFACTURAS")
        for factura in self.facturass:
            print(f"Cliente: {factura.cliente.nombre}")
            print(f"Fecha: {factura.fecha}")
            print(f"Total: ${factura.valor_total}\n")
        