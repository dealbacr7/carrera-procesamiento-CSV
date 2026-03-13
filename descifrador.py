import pandas as pd
import multiprocessing as mp

def descifrar_cesar(texto, desplazamiento=3):
    if not isinstance(texto, str):
        return texto
        
    return ''.join(
        chr(((ord(c) - 65 - desplazamiento) % 26) + 65) if c.isupper() else
        chr(((ord(c) - 97 - desplazamiento) % 26) + 97) if c.islower() else c
        for c in texto
    )

def procesar_chunk(chunk):
    chunk['nombre'] = chunk['nombre'].apply(descifrar_cesar)
    return chunk

def main():
    archivo_entrada = 'datos.csv' 
    tamano_chunk = 100000 
    
    chunks = pd.read_csv(archivo_entrada, chunksize=tamano_chunk)
    num_cores = mp.cpu_count()
    
    with mp.Pool(processes=num_cores) as pool:
        resultados = pool.map(procesar_chunk, chunks)
        
    df_descifrado = pd.concat(resultados, ignore_index=True)
    
    faustos_count = df_descifrado['nombre'].str.contains('Fausto', case=False, na=False).sum()
    
    print(f"El número de personas que se llaman Fausto es: {faustos_count}")

if __name__ == '__main__':
    main()