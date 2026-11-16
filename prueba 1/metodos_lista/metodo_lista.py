#creando una lista con list()
lista = list(["robert" , "tiene" , 18])

#devuelve la cantidad de elementos
cuenta_de_lista =len(lista)

#agregando un elemento a la lista append
lista.append (36)

#agregando un elemento a la lista en un indice especifico
lista.insert (3 , "años")


#agregando varios elemento a la lista 
lista.extend (["JAJAJAJJ" , "ya es 2026"])

#elimina un elemento de la lista (por su indice)
lista.pop (2)

#removiendo un elemento de la lista (por su valor)
lista.remove ("robert")

#eliminando todos los elementos de la lista
#lista.clear()

#ordena la lista (si usamos el parametro reverse=True lo ordena al revez   )
#lista.sort(reverse=True)

#inivierte los elementos de una lista
lista.reverse()



print (lista)