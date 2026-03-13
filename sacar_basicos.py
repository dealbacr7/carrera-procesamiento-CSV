def sacar_basicos(df):
    # El Jefe ya ha limpiado la columna 'salario' antes de pasarnos el df
    suma_salarios = df['salario'].sum()

    # Suma las edades
    suma_edades = df['edad'].sum()

    # Cuenta las personas (número de filas)
    total_gente = len(df)

    # Cuenta los parados (filtra los que están en estado 'parado')
    # Nota: Aseguraos de que la columna se llama 'estado' o 'parado_sn' según vuestro CSV
    parados = (df['estado'] == 'parado').sum()

    # Devuelve los datos
    return {
        "salarios": suma_salarios,
        "edades": suma_edades,
        "personas": total_gente,
        "parados": parados
    }