import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv("archivos_problemas_graficos\\fuente_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#obteniendo el total de ingresos
ingresos_totales = df["ingresos"].sum()

#mostrando el total 
print(f"el total de ingresos es de: ${ingresos_totales}")

#mostrando el grafico
plt.show()
