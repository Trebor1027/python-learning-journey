
#cambiando el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resuletos\\archivo2.csv")

#convertir a "str" los datos de una columna
df["edad"] = df["edad"].astype(str)

#mostrando el tipo de dato de una columna
#print(type(df["edad"][0]))

#reemplazando los datos de dalto por maestro
df["apellido"].replace("dalto","maestro",inplace=True) 

print(df)

#eliminando las filas con datos faltantes, (el axis=1 es para eliminar columnas y el axis=0 es para eliminar filas)
#df = df.dropna(axis=1)

#eliminando las filas repetidas
df = df.drop_duplicates()

df.to_csv("archivos_problemas_resuletos\\archivo_limpios.csv")