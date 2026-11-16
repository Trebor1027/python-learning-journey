
#usando open para abrir un archivo con una codificacion universal (UFT-8)
archivo_sin_leer = open("archivos_txt\\gracias_dalto.txt",encoding= "UTF-8")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una linea especifica
linea = archivo_sin_leer.readline()

archivo_sin_leer.close

print(linea)


