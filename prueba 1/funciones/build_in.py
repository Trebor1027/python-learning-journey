numeros = [4,7,1,42,15]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
#print(numero_mas_alto)

#encontrando el numero bajo de una lista
numero_mas_bajo = min(numeros)
#print(numero_mas_bajo)

#redondeando  a 6 decimales}
numero = round(12.67546, 2)
print(numero)

#retorna false = 0, vacio, false, None | true = distinto a 0, true, cadena de texto o datos no vacios
numero = bool(0)
print (numero)

#retorna true si todos los valores son verdaderos

resultado_all = all([[],245,"true",[453]])

print(resultado_all)

#suma todos los valores de un iterable

suma_total = sum(numeros)

print(suma_total)
