#creando una funcion que suma numeros
def suma():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a =input("dime tu primer numero: ")
        b =input("dime tu segundo numero: ")
        
        #intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
           
        #si lanzo una excepcion pedirle que ingrese los datos/el EXception es el obejto de todos las Excepciones no necesariamente se tiene que usar
        except Exception as e:
            print("te pedi un numero bro")
            print(f"ERROR: {(e)}")
        
        #si todo salio bien termina el bucle
        else:
            break
        #finally se ejecuta siempre
        finally:
            print("manejo de excepcion finalizado")
    #mostrando el resultado
    return resultado

print(suma())