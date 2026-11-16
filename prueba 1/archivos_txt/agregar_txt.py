with open("archivos_txt\\gracias_dalto.txt","a",encoding= "UTF-8") as archivo:
    
    #agregando un archivo con "a" al archivo
    for i in range(5):
        archivo.write(f"linea {i*+1} agregada\n")