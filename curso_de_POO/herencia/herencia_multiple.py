class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("hola, estoy hablando")
        
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
        
class Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return (f"mi hablidad es {self.habilidad}")
        
#creando un clase multiple que herede de (Persona,Artista)
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre,edad,nacionalidad,habilidad,salario,empresa):
#en vez de super() se usa la clase que se quiere agregar a la clase nueva ejem(Persona.__init())
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    
    #crando metodo presentarse
    def presentarse(self):
        print( f"hola soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en la {self.empresa}")
    

#creando clase
robert = EmpleadoArtista("robert",18,"venezolano","programar",500,"tagleatella")

#imprimiendo un metodo de la clase EmpleadoArtista
robert.presentarse()

#mostrando si una clase hereda de otra si estuviera en otro modulo
herencia = issubclass(EmpleadoArtista,Artista)
#mostrando si el objeto robert es una instacia de la clase EmpleadoArtista
instacia = isinstance(robert,EmpleadoArtista)
print(instacia)