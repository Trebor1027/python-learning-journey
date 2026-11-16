import re

#la cadena de la que se busca los patrones
text = "la fecha es 23/03/2021 y el  telefono es +1-555-555-5555"

#el patron a buscar 
pattern = r"\d{2}/\d{2}/\d{4}"

#el texto con el cual se reemplazara el patron
replacement = "(-----------) "

#reemplazar todas las apariciones  del patron en la cadena de texto
new_text = re.sub(pattern, replacement, text)

#imprimir el resultado
print("texto modificado:" , new_text)
