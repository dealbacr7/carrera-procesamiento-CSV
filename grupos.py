import pandas as pd

def agrupar_datos(df):
    # El Jefe ya ha limpiado la columna 'salario', así que la usamos directamente

    # 1. Agrupar por ciudades 
    dinero_ciudades = df.groupby('ciudad')['salario'].sum().to_dict()

    # 2. Crear los rangos de edad (bins de 5 años)
    rangos_etarios = pd.cut(df['edad'], bins=range(0, 115, 5), right=False)

    # 3. Agrupar salarios por rangos de edad
    # observed=False evita errores en versiones modernas de pandas
    dinero_edades = df.groupby(rangos_etarios, observed=False)['salario'].sum()
    
    # 4. Convertimos a diccionario con claves tipo string para el Jefe
    dinero_edades_dict = {str(k): v for k, v in dinero_edades.to_dict().items()}

    return {
        "ciudades": dinero_ciudades, 
        "edades": dinero_edades_dict
    }