lista_nombres = ["robert","dalto","lisseth"]
lista_apellidos =["rivas","curso","guerra"]


with open("archivos_problemas_resuletos\\archivo_resuelto","w") as archivo:
    archivo.writelines("los datos son:\n\n")
    [archivo.writelines(f"nombre: {n}\napellido: {a}\n---------\n")for n,a in zip(lista_nombres,lista_apellidos)]
