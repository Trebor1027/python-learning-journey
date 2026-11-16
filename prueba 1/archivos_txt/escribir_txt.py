with open("archivos_txt\\gracias_dalto.txt","w",encoding= "UTF-8") as archivo:
    #sobre escribiendo el archivo
    #archivo.write("eres increible master")
    
    #agregando 2 lineas con writelines
    archivo.writelines(["hola maestro como estas\n","yuca?\n"])
    
    #agregando otras 2 lineas con writelines
    archivo.writelines(["hola maestro como estas\n","yuca?\n"])