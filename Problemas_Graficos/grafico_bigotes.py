import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Problemas_Graficos\\categoria&valor.csv')
#print(df)

#creando un grafico de bigotes con los datos de df
sns.boxplot(x='categoria',y='valor', data=df)

#mostrando el grafico
plt.show()