#creando una funcion que muestre la serie fribonaci entre 0 y el numero dado

def fribonaci(num):
    a,b = 0,1
    fribonaci_lista = [0]
    for i in range(num):
        if b > num: return fribonaci_lista
        else: 
            fribonaci_lista.append(b)
            a,b = b,a+b
   
resultado_fribonaci = fribonaci(30)
print(resultado_fribonaci)
        
        
        
        
 #(> , <)