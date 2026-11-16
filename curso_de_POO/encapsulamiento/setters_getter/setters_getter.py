class Persona():
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre


robert = Persona("roberto",18)

nombre = robert.get_nombre()    
print(nombre)

robert.set_nombre("robert")

nombre = robert.get_nombre()    
print(nombre)




        