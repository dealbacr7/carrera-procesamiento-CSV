import pandas as pd
import numpy as np

def agrupar_datos(df):
    # 1. Limpieza rápida: Convertimos 'salario' a número. 
    # Los que dicen "PARADO" se convertirán en NaN (Not a Number)
    df['salario_num'] = pd.to_numeric(df['salario'], errors='coerce').fillna(0)

    # 2. Agrupar por ciudades usando la columna limpia
    dinero_ciudades = df.groupby('ciudad')['salario_num'].sum().to_dict()

    # 3. Crear los rangos de edad (bins de 5 años)
    # Usamos de 0 a 110 para asegurar que entren todos
    rangos_etarios = pd.cut(df['edad'], bins=range(0, 115, 5), right=False)

    # 4. Agrupar salarios por rangos de edad
    # observed=False evita errores en versiones modernas de pandas
    dinero_edades = df.groupby(rangos_etarios, observed=False)['salario_num'].sum()
    
    # Convertimos a diccionario con claves tipo string para el Jefe
    dinero_edades_dict = {str(k): v for k, v in dinero_edades.to_dict().items()}

    return {
        "ciudades": dinero_ciudades, 
        "edades": dinero_edades_dict
    }