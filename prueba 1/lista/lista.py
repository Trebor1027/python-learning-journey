  #(> , <)
  
lista_compras = []

for i in range(5):
    producto = input(f"ingrese producto {i+1}: ")
    
    lista_compras.append(producto)
    
    
print(f"tus productos son:, {lista_compras}")