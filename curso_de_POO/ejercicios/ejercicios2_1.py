class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad,)
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def presentacion_grado(self):
        print(f"Grado: {self.grado}")
        
        
p = Estudiante("robert",18,"sexto")
        
p.mostrar_datos()
p.presentacion_grado()