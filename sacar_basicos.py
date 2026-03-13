def sacar_basicos(df):
    # El Jefe ya ha limpiado la columna 'salario' y contado los parados.
    # Solo sumamos lo basico.
    suma_salarios = df['salario'].sum()
    suma_edades = df['edad'].sum()
    total_gente = len(df)

    return {
        "salarios": suma_salarios,
        "edades": suma_edades,
        "personas": total_gente
    }