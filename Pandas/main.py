from api.api import leer_excel,filtrar
from ui.ui import menu_principal, mostrar_resultados

def main():
    dataFrame = leer_excel()

    if dataFrame is None:
        print("No se pudo abrir el archivo.")
        return
    
    while True:
        resultado_menu = menu_principal()

        if resultado_menu is None:
            print("Saliendo...")
            break

        departamento,municipio,cultivo,num_registros = resultado_menu
        filtrar_datos = filtrar(departamento,municipio,cultivo,num_registros,dataFrame)
        
        if filtrar_datos is not None:
            mostrar_resultados(filtrar_datos)
            

main()