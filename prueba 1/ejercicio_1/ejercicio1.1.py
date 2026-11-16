
#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_pro = 4
dalto_curso = 1.5

#duracion de crudo

crudo_promedio = 5
crudo_dalto =  3.5


duracion_curso_min = round(100 - dalto_curso / otros_cursos_min *100, 2)
duracion_curso_max = 100 -dalto_curso*100 // otros_cursos_max
duracion_curso_pro = 100 - dalto_curso / otros_cursos_pro *100

#calculo de crudo
duracion_crudo = 100 - otros_cursos_pro * 1000// crudo_promedio /10
duracion_crudo_dalto =  100 - dalto_curso* 1000// crudo_dalto /10


print("-------A---------")
print (f"el curso de dalto tiene una diferencia de {(duracion_curso_min)}% menos que el mas rapido")
print (f"el curso de dalto tiene una diferencia de {duracion_curso_max}% menos que el mas lento")
print (f"el curso de dalto tiene una diferencia de {duracion_curso_pro}% menos que el promedio")


#resultado de crudo

print("-------b---------")

print (f"el crudo de un curso pormedio se elmina un {duracion_crudo}% de tiempo vacio")
print (f"el crudo del curso de dalto se elmina un {duracion_crudo_dalto}% de tiempo vacio")




#mostando diferencias si los cursos durante 10 horas

print("-------C---------")

print (f"ver 10 horas de este curso de dalt0 equivale a ver {otros_cursos_pro * 100 //dalto_curso / 10} horas de otros cursos")
print (f"ver 10 horas de un curso promedio equivale a ver {dalto_curso * 100 //otros_cursos_pro / 10} horas del cursos de dalto")
