import pandas as pd
import multiprocessing as mp
import time
from collections import Counter

# 1. IMPORTAMOS A TUS TRABAJADORES
import sacar_basicos
import grupos
import descifrador
import votos

# 2. LA FUNCION QUE SE EJECUTA EN CADA TROZO (CHUNK)
def procesar_un_trozo(chunk):
    parados_en_este_trozo = (chunk['salario'] == 'PARADO').sum()
    chunk['salario'] = pd.to_numeric(chunk['salario'], errors='coerce').fillna(0)
    
    res_basicos = sacar_basicos.sacar_basicos(chunk)
    res_basicos['parados'] = parados_en_este_trozo
    
    res_grupos = grupos.agrupar_datos(chunk)
    res_nombres = descifrador.buscar_nombres(chunk)
    res_votos = votos.contar_votos(chunk)
    
    return {
        "basicos": res_basicos,
        "grupos": res_grupos,
        "nombres": res_nombres,
        "votos": res_votos
    }

# 3. EL MOTOR PRINCIPAL (EL ENSAMBLAJE)
if __name__ == '__main__':
    inicio = time.time()
    print("Arrancando motores... Procesando 10 millones de filas...")

    archivo_csv = "datos.csv"
    tamano_trozo = 500000 
    
    lector_chunks = pd.read_csv(archivo_csv, chunksize=tamano_trozo)

    total_salarios = 0
    total_edades = 0
    total_personas = 0
    total_parados = 0
    total_faustos = 0
    total_tocayos = 0
    
    votos_totales = Counter()
    ciudades_totales = Counter()
    edades_totales = Counter()
    detalle_tocayos_total = Counter() # Nuevo contador para el detalle

    nucleos = mp.cpu_count()
    with mp.Pool(processes=nucleos) as pool:
        for resultado_trozo in pool.imap_unordered(procesar_un_trozo, lector_chunks):
            
            total_salarios += resultado_trozo['basicos']['salarios']
            total_edades += resultado_trozo['basicos']['edades']
            total_personas += resultado_trozo['basicos']['personas']
            total_parados += resultado_trozo['basicos']['parados']
            
            total_faustos += resultado_trozo['nombres']['faustos']
            total_tocayos += resultado_trozo['nombres']['total_tocayos']
            
            # Sumamos los detalles de los tocayos de este trozo
            detalle_tocayos_total.update(resultado_trozo['nombres']['detalle_tocayos'])
            
            votos_totales.update(resultado_trozo['votos'])
            ciudades_totales.update(resultado_trozo['grupos']['ciudades'])
            edades_totales.update(resultado_trozo['grupos']['edades'])
            
            print(f"Un trozo procesado. Llevamos {total_personas} personas...")

    print("\nLectura terminada. Calculando metricas finales...")

    salario_medio = total_salarios / total_personas if total_personas > 0 else 0
    edad_media = total_edades / total_personas if total_personas > 0 else 0
    
    ciudades_ordenadas = ciudades_totales.most_common()
    top_3_ricas = ciudades_ordenadas[:3] 
    top_3_pobres = ciudades_ordenadas[-3:] 
    
    rango_rico = edades_totales.most_common(1)[0] if edades_totales else ("Ninguno", 0)
    
    coalicion_ganadora = votos.calcular_ganador(dict(votos_totales))

    fin = time.time()

    print("\n" + "="*50)
    print("RESULTADOS DEL ANALISIS")
    print("="*50)
    print(f"Tiempo total: {round(fin - inicio, 2)} segundos")
    print(f"Total personas procesadas: {total_personas}")
    print(f"Salario Medio: {round(salario_medio, 2)}")
    print(f"Edad Media: {round(edad_media, 2)} años")
    print(f"Rango de edad con mayor salario: {rango_rico[0]} (Total: {round(rango_rico[1], 2)})")
    print(f"Combinacion ganadora de elecciones: {coalicion_ganadora}")
    print(f"Faustos encontrados: {total_faustos}")
    print(f"Desglose de Tocayos encontrados:")
    
    # Imprimimos cada nombre individualmente
    for nombre, cantidad in detalle_tocayos_total.items():
        print(f"  - {nombre}: {cantidad}")
        
    print(f"Total de Tocayos en el grupo: {total_tocayos}")
    print(f"Top 3 Ciudades mas RICAS: {top_3_ricas}")
    print(f"Top 3 Ciudades mas POBRES: {top_3_pobres}")
    print(f"Numero de parados: {total_parados}")
    print("="*50)