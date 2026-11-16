
#abrimos el archivo con with open
with open("archivos_txt\\gracias_dalto.txt",encoding= "UTF-8") as archivo:

    #leemos el archivo
    archivo.read
    
    #mostramos el archivo
    print(archivo.read())

#no es necesario leer el archivo con with open