#importando un modulo y asignandole m_saludar 
import modulo_saludar as m_saludar

#desde ese modulo importamos 2 funciones
#tambien se puede usar el (import*) para importar todo
#from modulo_saludar import saludar

#creamos las variables con los resultados
#saludo = saludar("robert")


#mostramos los resultados
#print(saludo)



#para ver las propiedades  y metodos del namespace
print(dir(m_saludar))
 
 
 #acedemos al nombre de este modulo
print(__name__)