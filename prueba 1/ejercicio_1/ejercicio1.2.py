frase = input("dime una frase y te calculo el tiempo que tardas en decirla apa: ")

palabras_separadas = frase.split (" ")
cantidad_palabras_separadas = len(palabras_separadas)

if cantidad_palabras_separadas > 120:
    print("bro deja de hablar canto ve cerrando el ortito")


print(f"dijiste : {cantidad_palabras_separadas} palabras y tardarias {cantidad_palabras_separadas/2} segundos decirlo")
print (f"dalto lo diria en {cantidad_palabras_separadas * 100 // 2 *1.3 / 100} segundos")



     #(> , <)

