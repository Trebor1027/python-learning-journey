#el mro es baiscamnete como python sigue la gerarquia de las herencias
class A:
    def hablar(self):
        print("hola soy A")
     
class F:
    def hablar(self):
        print("hola soy F")
        
class B(A):
    def hablar(self):
        print("hola soy B")
        
class C(F):
    def hablar(self):
        print("hola soy C")

class D(B,C):
    def hablar(self):
        print("hola soy D")
        

d = D()

d.hablar()

F.hablar(d)