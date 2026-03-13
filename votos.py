import pandas as pd

def contar_votos(df):
    votos = df['partido'].value_counts().to_dict()
    return votos


def calcular_ganador(votos_totales_diccionario):

    # calcular total de votos
    total_votos = sum(votos_totales_diccionario.values())

    # calcular mayoría absoluta
    mayoria_absoluta = (total_votos // 2) + 1

    # ordenar partidos de mayor a menor votos
    partidos_ordenados = sorted(votos_totales_diccionario.items(), key=lambda x: x[1],reverse=True)

    # construir coalición
    coalicion = []
    suma_votos = 0

    for partido, votos in partidos_ordenados:
        coalicion.append(partido)
        suma_votos += votos

        if suma_votos >= mayoria_absoluta:
            break

    return coalicion