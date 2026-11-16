#creando una funcion que nos devuelva nos numeros primos 
#entre 0 y el argumento que le pasamos 


#creando una funcion que verifica si el numeor es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y el mismo numero -1
    for i in range(2,num-1):
        #si es divisible retornamos falso y termina el bucle
        if num%i==0: return False
        #si termina el bucle significa que no fue divisible entonces es primo
        return True
    
#creando una funcion que retorne una lista con todos los numeros primos    
def primos_hasta(num):
    #crando una lista vacia para los numeors primos
    primos = []
    
    for i in range(3,num+1):
        #verificamos que sea primo
        resultado =es_primo(i)
        #en caso de que sea primo se agrega a la lista
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos
#cramos el resultado llamando a la funcion y la mostamos
resultado =primos_hasta(98)
print(resultado)