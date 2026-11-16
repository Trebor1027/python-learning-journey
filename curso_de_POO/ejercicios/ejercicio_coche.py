class Coche:
    def __init__(self,marca,modelo,velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        
    def acelerar(self):
        self.velocidad +=10
        print(f"la velocidad ahora es: {self.velocidad}")
        
    def frenar(self):
        self.velocidad -=5
        print(f"la velocidad ahora es: {self.velocidad}")
        
    def mostrando_datos(self):
        print(f"tu coche es un: {self.marca} y es un modelo: {self.modelo} y su velocidad principal es de: {self.velocidad}")
        
        
coche = Coche("Toyota","Supra",5)

coche.acelerar()
coche.frenar()
coche.mostrando_datos()
        
        
class CarroDeportivo(Coche):
    def __init__(self,marca,modelo,velocidad,MarcaDeportiva):
        Coche.__init__(self,marca,modelo,velocidad)
        self.MarcaDeportiva = MarcaDeportiva
        
    def presentar_coche(self):
        print(f"este {self.marca} {self.modelo}")

supra = CarroDeportivo("supra","mk4",300,"mi marca")

print(supra.presentar_coche())

        
        
        
    
