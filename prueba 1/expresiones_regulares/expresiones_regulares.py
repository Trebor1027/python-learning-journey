import re 

texto ="""hola maestro. esta es la cadena 1. como estas mi capitan
esta es la linea 2 323 abab de texto.
y esta es la ultima linea (linea 3)

"""
#haciendo una busqueda simple
#resultado = re.search("hola",texto)
#resultado = re.findall("hola",texto)

#\d = busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d",texto)

#\D = busca  TODO menos digitos numericos del 0 - 9
#resultado = re.findall(r"\D",texto)

#\w = busca caracteres alfanumericos [a-z, A-Z, 0-9, _]
#resultado = re.findall(r"\w",texto)

#\W = busca TODO menos caracteres alfanumericos [a-z, A-Z, 0-9, _]
#resultado = re.findall(r"\W",texto)

#\s busca espacios en blanco = espacios, tabs, saltos en linea
#resultado = re.findall(r"\s",texto)

#\S busca TODO menos espacios en blanco = espacios, tabs, saltos en linea
#resultado = re.findall(r"\S",texto)

#busca TODO menos saltos en linea
#resultado = re.findall(r".",texto)

#\n busca saltos en linea
#resultado = re.findall(r"\n",texto)

#\ cancelamos caracteres especiales/ cancelando la funcion del punto  y buscamos  puntos
#resultado = re.findall(r"\.",texto)  

#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r"\d\.\s",texto)

#^ buscando el comienzo de una linea
#resultado = re.findall(r"^hola maestro",texto)

#flags=re.M = activa la multi linea
#resultado = re.findall(r"^hola maestro" ,texto,flags=re.M)

#$ buscando el final de una linea
#resultado = re.findall(r"capitan$",texto,flags=re.M)

#{n} busca n cantidad de veces el  valor de la izquierda
resultado = re.findall(r"\d{3}\s",texto,)


#{n,m} al menos (n), como maximo (m)
resultado = re.findall(r"\d{2,4}\s",texto,)

#
resultado = re.findall(r"(ab){2}",texto,)
#
resultado = re.findall(r"[ab]{2}",texto,) 

#|  busca una cosa o la otra
resultado = re.findall(r"\d{2,4}|hola",texto,)





print(resultado)



#\