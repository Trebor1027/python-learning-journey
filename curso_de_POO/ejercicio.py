binario = input("Número binario a decimal: ")

    
def binario_a_decimal(binario):
    resultado = 0
    posicion = 0

    for digito in reversed(binario):
        resultado += int(digito) * (2 ** posicion)
        posicion += 1

    return resultado
    

print(binario_a_decimal(binario))
        
  

    