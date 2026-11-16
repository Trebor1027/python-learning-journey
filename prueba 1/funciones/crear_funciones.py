#creando una funcion simple

#def saludar():
    
    #print("hola master como andas")
#ejecutando la funcion simple
#saludar()

#creando una funcion con parametros
#nombre = input("ingresa tu nombre: ")

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "rey"
    else:
        adjetivo = "crak"
    
          
    print(f"hola {nombre} como estas mi {adjetivo}?")

saludar("lisseth","mujer")
saludar("robert","hombre")
saludar("fran","no binario")

#creando contraseña random

def contraseña_random(numero):
    caracteres = "abcdfghij"
    numero_entero = str(numero)
    numero = int(numero_entero[0])
    c1 = numero -2
    c2 = numero 
    c3 = numero -5
    contraseña = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{numero*2}"
    return contraseña,numero

contraseña,primer_numero = contraseña_random(36865)


print(f"tu contraseña nueva es: {contraseña}")
print(f"y el numero base fue: {primer_numero}")

      
    