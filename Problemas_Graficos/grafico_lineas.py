import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Problemas_Graficos\\pedos.csv')
#print(df)

#creando un grafico de lineas con los datos de df
sns.lineplot(x='fecha',y='pedos', data=df)
#creando un punto en el dia que hubo mas pedos
plt.plot('01-04',5,'o')
#mostrando el grafico
plt.show()