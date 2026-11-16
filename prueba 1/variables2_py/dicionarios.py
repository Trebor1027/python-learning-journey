#creando dicionario con dict
dicionario = dict (nombre= "robert", apellido= "carlos")

print(dicionario)

#las listas no pueden ser claves y usamos frozenset para meter conjuntos

dicionario = {frozenset(["nombre", "apellido"]):"jajajjaj"}

print(dicionario)





#creando dicionario con fromkeys

dicionario = dict.fromkeys(["nombre","apellido"])

#creando dicionario con fromkeys valor por defecto: nose

dicionario = dict.fromkeys(["nombre","apellido"],"nose")

print(dicionario)