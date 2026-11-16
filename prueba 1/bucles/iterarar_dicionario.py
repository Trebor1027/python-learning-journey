diccionario = {
    "nombre": "lucas",
    "apellido": "torres",
    "edad" : 18
}

#recorriendo un diccionario con item() para obtener la clave y el valor
for key in diccionario.items():
    print(key) 
    
#recorriendo un diccionario con item() para obtener la clave y el valor
for datos in diccionario.items(): 
    key = datos[0]
    valor = datos[1]
    
    print(f"la clave es: {key}\nel valor es: {valor}") 