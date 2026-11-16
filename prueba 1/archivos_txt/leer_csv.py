import csv

with open("archivos_txt\\archivo.csv") as archivo: 
    reader = csv.reader(archivo)
    for row in reader:
        print(row)