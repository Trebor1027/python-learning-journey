
#esta clase es difente a la primera ya que podemos crear varios objetos con la misma clase
class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
#los metodos son funcion que puede hacer el objeto
        
    def foto(self):
        print("tomaste una foto") 
        
    def llamar(self):
        print(f"estas haciendo un llamado desde tu: {self.modelo}")
        
    def cortar(self):
        print(f"cortaste la llamda desde tu: {self.modelo}")

celular1 =Celular("samsung","S24","48MP")
celular2 =Celular("Apple","Iphon 15","98MP")
    
celular1.foto()
celular1.llamar()
