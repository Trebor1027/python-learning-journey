binario = input("Número binario a decimal: ")
binario_int = int(binario)
    
def binario_a_hexadecimal(binario_int):
    resultado = 0
    posicion = 0

    for digito in reversed(binario_int):
        resultado += (digito) * (16 ** posicion)
        posicion += 1

    return resultado
    

print(binario_a_hexadecimal(binario))
        