import csv

def agregar_escritura(ruta_archivo, datos):
    with open(ruta_archivo, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(datos)
        
agregar_escritura("archivos_txt/archivo.csv", [])