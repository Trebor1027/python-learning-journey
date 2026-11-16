import random

numero_secreto = random.randint (1,10)

while True:
    intento = int(input("adivina el numero del (1.10): "))
    
    if intento > numero_secreto:
        print ("el numero es menor")
    elif intento < numero_secreto:
        print("el numero es mayor")
    
    else:
        print("ganaste")
        break

    
    
     #(> , <)