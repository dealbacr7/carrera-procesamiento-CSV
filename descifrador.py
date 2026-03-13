# descifrador.py

# 1. Función para CIFRAR (al revés que descifrar)
def cifrar_cesar(texto, desplazamiento=3):
    if not isinstance(texto, str):
        return texto
    return ''.join(
        chr(((ord(c) - 65 + desplazamiento) % 26) + 65) if c.isupper() else
        chr(((ord(c) - 97 + desplazamiento) % 26) + 97) if c.islower() else c
        for c in texto
    )

# 2. Preparamos las palabras clave cifradas UNA SOLA VEZ
nombres_grupo = ['Fausto', 'Rafael', 'David', 'Paula', 'Lucia']
# Las pasamos por la encriptación para buscar su versión "rara"
nombres_cifrados = [cifrar_cesar(nombre) for nombre in nombres_grupo]

# 3. La función que usará el Jefe para cada trozo
def buscar_nombres(df):
    # Contamos Faustos (el primer nombre de la lista)
    fausto_cifrado = nombres_cifrados[0]
    num_faustos = (df['nombre'] == fausto_cifrado).sum()
    
    # Contamos los tocayos del grupo (todos menos Fausto, asumiendo que Fausto no es del grupo)
    tocayos_cifrados = nombres_cifrados[1:] 
    num_tocayos = df['nombre'].isin(tocayos_cifrados).sum()
    
    return {
        "faustos": num_faustos,
        "tocayos": num_tocayos
    }