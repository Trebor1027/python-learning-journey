#falto el profesor a clases y los alumnos van a armar la clase

#pedir nombre y edad a los alumnos


#funcion para obtener el asistente y el profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creadno la lista de compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre =input("ingrese su nombre: ")
        edad = int(input("ingrese su edad: "))
        compañero = (nombre,edad)
        
        #afregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key = lambda x:x[1]) 
   
   
   #compañeros[x] devuelve una tupla con nombre,edad y despues accede al nombre
   #para definir el asistente y el profesor
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(3)

print(f"el profesor de la clase es: {profesor} y su asistente es: {asistente}")
    
    
