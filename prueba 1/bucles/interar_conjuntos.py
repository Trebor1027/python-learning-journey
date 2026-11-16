animales={"perro","gato","loro","drilococo"}
numeros={10,86,56,77}

#recorriendo la conjuto de animales con for
for animal in animales:
    print(f"ahora la variable animal es: {animal}")
    
 #recorriendo la conjuto de los numeros y * 10
    
for numero in numeros:
    resultado = numero * 10
    print(f"ahora la variable de los numeros es: {resultado }")

#iterando dos conjutos al mismo tiempo

for numero,animale in zip(animales,numeros):
    print(f"recorriendo conjuto 1: {numero}")
    print(f"recorriendo conjuto 2: {animale}")
    
#ejecutando numeros en un rango determinado

for num1 in range(0,10, 2):
    print(num1)
    

#forma correcta de recorrer una conjuto

for num in enumerate(numeros):
    indice = num [0]
    valor = num [1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#usando el for/else
for numero in numeros:
      print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")