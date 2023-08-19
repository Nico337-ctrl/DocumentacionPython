import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Problemas_Graficos\\plata.csv')
#print(df)

#creando un grafico de barras con los datos de df
sns.barplot(x='fuente',y='ingresos', data=df)

total_ingresos = df['ingressos'].sum()
#mostrando el total en ingresos
print(f'Total ingresos: ${total_ingresos} USD')
#mostrando el grafico
plt.show()