
#crando una excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"cometiste el siguiente error: {err}")
        
#lanzando mi propia excepcion
#raise MiExcepcion("jajajaja,tontillo")

#manejandola
try:
    raise MiExcepcion("(hola persona medio tarada)")

except:
    print("como vas a manejar ese error")