import pandas as pd
import os

def leer_excel():
    direccion_actual = os.path.dirname(os.path.abspath(__file__))
    raiz_proyecto = os.path.dirname(direccion_actual)
    ruta_archivo = os.path.join(raiz_proyecto,'data','resultado_laboratorio_suelo.xlsx')

    try:
        df = pd.read_excel(ruta_archivo)

        columnas_a_convertidas = ["pH","Fósforo(P)","Potasio(K)"]
        df[columnas_a_convertidas] = df[columnas_a_convertidas].apply(pd.to_numeric,errors="coerce")

        return df
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return None



def filtrar(departamento,municipio,cultivo,num_registros,archivo):

    df = archivo

    filtrado = ((df['Departamento'] == departamento) & (df['Municipio'] == municipio) &  
               (df['Cultivo'] == cultivo))
    
    if filtrado.any():
        df = df[filtrado]
        mediana_ph = df['pH'].median()
        media_fosforo = df['Fósforo(P)'].median()
        media_potasio = df['Potasio(K)'].median()
        registros = df.head(num_registros)

        return {
            "registros": registros,
            "Mediana pH": mediana_ph,
            "Mediana Fosforo": media_fosforo,
            "Mediana Potasio":media_potasio
        }
    else:
        print(f"No se encontro ningun registro los datos ingresados.")
        return None

