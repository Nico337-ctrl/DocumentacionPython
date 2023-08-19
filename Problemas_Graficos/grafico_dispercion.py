import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Problemas_Graficos\\tmp&dinero.csv')
#print(df)

#creando un grafico de dispercion con los datos de df
sns.scatterplot(x='tiempo',y='dinero', data=df)

#mostrando el grafico
plt.show()