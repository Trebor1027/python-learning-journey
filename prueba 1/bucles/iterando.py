#creado listas

frutas = ["manzana", "pera","nueces","naranja"]
cadena = "hola"
numeros =[2,5,8,10]
#evitando q se coma una pera con la sentencia continue
for fruta in frutas:
    if fruta == "pera":
       continue    
    print(f"me voy a comer una {fruta}")
    
    #evitar que el bucle se siga ejecutando
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "nueces":
        break  
else:
    print("termino")  
   

print("bucle terminado, me callo mal las nueces")


#recorrer una cadena de texto

for letra in cadena:
    print(letra)
    

#for con list
numeros_duplicados = list()

for numero in numeros:
    numeros_duplicados.append(numero * 2)
    if len(numeros_duplicados) == 4:
        print(f"si che aqui esta tu numerito que es el")
print(numeros_duplicados)



#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)