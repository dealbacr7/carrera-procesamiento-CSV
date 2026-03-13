import pandas as pd

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
    
    # AHORA USAMOS str.contains() PARA BUSCAR DENTRO DEL NOMBRE Y APELLIDOS
    num_faustos = df['nombre'].str.contains(fausto_cifrado, case=False, na=False).sum()
    
    # Contamos los tocayos del grupo
    num_tocayos = 0
    tocayos_cifrados = nombres_cifrados[1:] 
    
    for tocayo in tocayos_cifrados:
        num_tocayos += df['nombre'].str.contains(tocayo, case=False, na=False).sum()
    
    return {
        "faustos": num_faustos,
        "tocayos": num_tocayos
    }