#creando una clase llamada gato
class Gato():
#creando un metodo de sonido
    def sonido(self):
        return "Miau"
#creando una clase llamada gato
class Perro():
#creando un metodo de sonido
    def sonido(self):
        return "Guau"

#creando un solo metodo para varias clases (gato/perro) para que reproduca el sonido
#basicamente esto es el polimorfismo
def animal_sonido(animal):
    print(animal.sonido())

#creando una instancia
gato = Gato()
perro = Perro()

#reproduciendo el sonido con un solo metodo
animal_sonido(gato)
