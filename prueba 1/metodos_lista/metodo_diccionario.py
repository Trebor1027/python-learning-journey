diccionario = {
    
    "nombre" : "robert",
    "edad" : "18",
    "vive" : "Asturias"    
}

#nos devuleve un objeto dict_item

#clave = diccionario.keys()

#print (clave)


#obteniedo un elemento con get() (si no se encuentra el programa sigue)
diccionario = {
    
    "nombre" : "robert",
    "edad" : "18",
    "vive" : "Asturias"    
}

clave = diccionario.get("edad")

#elimina todo el dicionario
#diccionario.clear()

#eliminando un elemento del diccionario
#diccionario.pop("nombre")


#obteniedo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

print (diccionario_iterable)
