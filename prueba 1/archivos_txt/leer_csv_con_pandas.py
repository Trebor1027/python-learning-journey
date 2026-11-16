#importando la libreria pandas
import pandas as pd
df = pd.read_csv("archivos_txt\\archivo.csv")
df2 = pd.read_csv("archivos_txt\\archivo.csv")

#obteniendo los datos de la columna nombre
nombre =(df["nombre"])

#ordenando el dataframe ascendente
datos_ordenados = df.sort_values("edad",ascending=False)

#ordenando el dataframe descendiente
datos_ordenados = df.sort_values("edad")

#concatenando los 2 dataframe
df_concatenado = pd.concat([df,df2])

#acediendo a las primera 3 filas con head()
primer_fila = df.head(1)

#acediendo a las ultimas 3 filas con tail()
ultima_fila = df.tail(1)

#acediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del data frame:
df_info = df.describe()

#acediendo a un elemento del dataframe con loc
elemento_especifico_loc = df.loc[2,"nombre"]

#acediendo a un elemento del dataframe con iloc
elemento_especifico_loc = df.iloc[2,0]

#acediendo a todas los apellidos con iloc
apellidos = df.iloc[:,1]

#acediendo a la fila 3  con loc
fila_3 = df.loc[2,:]

#acediendo a la fila 3  con iloc
fila_3 = df.loc[2,:]

#acediendo a filas con edad mayoy a 20
mayor_que_27 = df.loc[df["edad"]>27,:]

print(mayor_que_27)







#cadena ="0123456789"
#print(cadena[:])