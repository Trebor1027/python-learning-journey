#forma no optima de sumar valores

#def sumar (lista):
 #   numeros_sumados = 0
  #  for numero in lista:
 #       numeros_sumados = numeros_sumados + numero
 #   return numeros_sumados
    
#resultado_de_suma = sumar([5,3,7,10,])
#print(resultado_de_suma)


#forma correcta de sumar numeros

def sumar (nombre,*numero):
    return f"hola {nombre} la suma de tus numeros es: {sum(numero)}"

resultado = sumar("lucas",5,3,7,10)
print(resultado)


#otras formas

def suma_total(numeros):
    return sum([*numeros])

resultado = suma_total([5,7,9,3])
print(resultado)
    
