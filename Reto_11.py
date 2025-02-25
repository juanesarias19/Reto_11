def contar_vocales_consonantes_y_palabras(ruta_archivo):
    with open(ruta_archivo, "r") as file:
        content = file.read().lower()
    
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    
    total_vocales = sum(content.count(v) for v in vocales)
    total_consonantes = sum(content.count(c) for c in consonantes)
    
    palabras = content.split()
    conteo_palabras = {}

    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1

    palabras_mas_comunes = sorted(conteo_palabras.items(), key=lambda x: x[1], reverse=True)[:5]
    
    print("Total de vocales en el archivo:", total_vocales)
    print("Total de consonantes en el archivo:", total_consonantes)
    
    print("Palabras más repetidas:")
    for palabra, cantidad in palabras_mas_comunes:
        print(f"{palabra}: {cantidad}")

# Uso de la función
ruta = r"C:\Users\juane\OneDrive\Escritorio\Universidad\Programacion\mbox.txt"
contar_vocales_consonantes_y_palabras(ruta)
