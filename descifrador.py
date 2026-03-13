import pandas as pd

# 1. Funcion para CIFRAR (al reves que descifrar)
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
nombres_cifrados = [cifrar_cesar(nombre) for nombre in nombres_grupo]

# 3. La funcion que usara el Jefe para cada trozo
def buscar_nombres(df):
    # Faustos (indice 0)
    fausto_cifrado = nombres_cifrados[0]
    num_faustos = int(df['nombre'].str.contains(fausto_cifrado, case=False, na=False).sum())
    
    # Detalle de tocayos del resto del grupo
    detalle_tocayos = {}
    total_tocayos = 0
    
    for i in range(1, len(nombres_grupo)):
        nombre_real = nombres_grupo[i]
        nombre_cifrado = nombres_cifrados[i]
        
        cantidad = int(df['nombre'].str.contains(nombre_cifrado, case=False, na=False).sum())
        detalle_tocayos[nombre_real] = cantidad
        total_tocayos += cantidad
    
    return {
        "faustos": num_faustos,
        "detalle_tocayos": detalle_tocayos,
        "total_tocayos": total_tocayos
    }