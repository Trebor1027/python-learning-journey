#crando la clase llamada estudiante

class estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grando = grado
    def estudiar(self):
        print("Estudiando...")
    
    def no_estudiar(self):
        print("seguro que quieres salir?")
        return quit
        
nombre = input("digame su nombre: ")
edad = input("digame su edad: ")
grado = input("en que grado estas: ")

estudiante_1 = estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE \n
      Nombre: {nombre}
      Edad: {edad} 
      Grado: {grado}
      """)
while True:
    estudiar = input("ingresa la palabra estudiar, si quiere estudiar: ")
    if (estudiar.lower() == "estudiar"):
    
        estudiante_1.estudiar()
    else:
        estudiar.lower == "no"
        estudiar.no_estudiar()
