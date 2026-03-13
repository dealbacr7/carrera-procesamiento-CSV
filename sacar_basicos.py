def sacar_basicos(df):
    # Suma los salarios
    suma_salarios = df['salario'].sum()

    # Suma las edades
    suma_edades = df['edad'].sum()

    # Cuenta las personas (número de filas)
    total_gente = len(df)

    # Cuenta los parados (filtra los que están en estado 'parado')
    parados = (df['estado'] == 'parado').sum()

    # Devuelve los datos en el formato solicitado
    return {
        "salarios": suma_salarios,
        "edades": suma_edades,
        "personas": total_gente,
        "parados": parados
    }
