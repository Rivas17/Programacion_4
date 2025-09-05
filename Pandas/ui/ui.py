def menu_principal():
    print("\n\tMenú Principal")
    print("1. Consultar propiedades edáficas: ")
    print("2. Salir")
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                departamento = input("Ingrese el departamento: ").upper()
                municipio = input("Ingrese el municipio: ").upper()
                cultivo = input("Ingrese el cultivo: ").capitalize()
                num_registros = int(input("Ingrese el numero de registros a consultar: "))

                return departamento,municipio,cultivo,num_registros
            else:
                return None
        except ValueError:
            print("Error. Ingrese un numero.")


def mostrar_resultados(diccionario_filtrados):
    if diccionario_filtrados is None:
        print("No se encontraron resultados para la consulta.")
        return
    
    df_registros = diccionario_filtrados['registros']
    mediana_ph = diccionario_filtrados['Mediana pH']
    mediana_fosforo = diccionario_filtrados['Mediana Fosforo']
    mediana_potasio = diccionario_filtrados['Mediana Potasio']

    #Agregamos al dataFrame
    df_registros['Mediana pH'] = mediana_ph
    df_registros['Mediana Fosforo'] = mediana_fosforo
    df_registros['Mediana Potasio'] = mediana_potasio

    columnas_finales = [
        'Departamento',
        'Municipio',
        'Cultivo',
        'Topografia',
        'Mediana pH',
        'Mediana Fosforo',
        'Mediana Potasio'
    ]

    df_final = df_registros[columnas_finales]

    print("------Resultados de la consulta------")
    print(df_final)




