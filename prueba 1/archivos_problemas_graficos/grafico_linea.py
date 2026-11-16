import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv("archivos_problemas_graficos\\pedos.csv")

#creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)

#mostrando cuando fue que se tiro mas pedos
plt.plot("01-09",17,"o")

#mostrando el grafico
plt.show()
