#creando un conjunto

conjunto = set(["dato 1"])

#metiendo un conjunto dentro de otro conjunto

conjunto_1 = frozenset(["dato 1", "dato 2"])
conjunto_2 = {conjunto_1, "dato 3"}

print (conjunto_2)


#teoria de conjuntos

conjunto_3 = {1,3,5,7}
conjunto_4 = {1,3,7}


#verificando si es un sub conjunto
#esultado1 = conjunto_4.issubset(conjunto_3)
#resultado2 = conjunto_4 <= conjunto_3

#print(resultado2)

#verificando si es un super conjunto
resultado1 = conjunto_4.issuperset(conjunto_3)
resultado2 = conjunto_4 > conjunto_3

#verificando si hay un numero igual en el conjunto

resultado2 = conjunto_4.isdisjoint(conjunto_3)

print(resultado2)
 #(> , <)