
numeros = [5,8,3,7,10,66]

#creando una funcion lambda para multiplicar
#multiplicar_por_dos = lambda x : x*2

#creando una funcion comun que diga si es par o no

#def par_num(numeros):
 #   if numeros%2==1:
#        return True
    
#usando filter con una funcion comun
#numeros_pares = filter(par_num,numeros)

#creadon lo mismo de antes pero con lambda
num_pares = filter(lambda numero: numero%2 ==0, numeros)

print(list(num_pares))