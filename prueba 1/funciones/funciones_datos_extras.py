#creando una funcion de 3 parametros


def frase (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido} eres muy {adjetivo}"

#usando keyword arguments 

saludo = frase( adjetivo= "capo", nombre ="robert", apellido = "rivas",)
print(saludo)