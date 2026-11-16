#esta clase es difente a la primera ya que podemos crear varios objetos con la misma clase
class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 =Celular("samsung","S24","48MP")
celular2 =Celular("Apple","Iphon 15","98MP")
    
celular1.foto()
celular1.llamar()

#self se utiliza para que la clase se refiera asi misma
