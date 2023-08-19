#importando la bibioteca pandas 
import pandas as pd

#leyendo el archivo csv
#la variable se llamada "df" por ser un dataframe
#a esta funcion "read_csv" se le puede agregar un parametro para renombrar las columnas del archivo, este parametro se llama "names"

df = pd.read_csv('ArchivosCSV\\archivo.csv')#, #names=['nombres', 'nombres', 'edades']) 
df.columns.str.strip()

#obteniendo los datos de la columna nombre 
"""
nombres = df['nombres']
#print(nombres)
"""


#Teoria del slising
#usando los ":" indicamos por donde comienza y donde termina la iteracion de algun elemento 
cadena_simple = '0123456789'
print(f'Mostrando una cadenas simple recorrida desde el 0 hasta el 7: {cadena_simple[0:7]}')


#ordenando el dataframe por la edad
df_ordenado = df.sort_values(['edad'])
#print(df_ordenado)


#codigo para verificar si las columnas existen
"""if 'edad' in df.columns:
    columna_edad = df['edad']
    print(columna_edad)
else:
    print('la columna edad no existe en el archivo csv')
"""

#contatenando los archivos csv 

df2 = pd.read_csv('ArchivosCSV\\archivo.csv')#, #names=['nombres', 'nombres', 'edades']) 

#De esta forma contatenamos dos archivos csv para utilizarlos para lo que querrramos 
df_contanenado = pd.concat([df, df2])
#print(df_contanenado)

#Ordenando archivos csv contatenados
df_contanenado_ord = df_contanenado.sort_values('edad')
#print(df_contanenado_ord)


#Accediendo a las primeras filas con el metodo head()
#El metodo head()
primera_fila = df.head(3)
print(f'Mostrando las primeras filas: \n{primera_fila}')

#Accediendo a las ultimas filas con el metodo tail()
#El metodo Tail()
ultima_fila = df.tail(3)
print(f'Mostrando las ultimas filas: \n{ultima_fila}')

#mostrando primeros y ultimos datos de archivos csv ordenados
ultimos_datos = df_contanenado_ord.tail(4)
primeros_datos = df_contanenado_ord.head(4)
print(f'Mostrando los ultimos datos del data frame ordenado: \n {ultimos_datos}')
print(f'Mostrando los primeros datos del data frame ordenado: \n {primeros_datos}\n')


#Mostrando la cantidad de filas y columnas que hay en el archivo
#Desempaquete la tupla que devuelve el parametro shape, en una ejecucion normal del codigo sin empaquetar retornaria esto "(5, 3)"
fila, columna = df.shape
print(f'Cantidad de filas que hay {fila} y columnas {columna}\n ')

#Mostrando y desempaquetando las filas y columnas de el data frame ordenado y concatenado
filasDFORD, columnasDFORD = df_contanenado_ord.shape
print(f'Mostrando el df ordenado contanenado: \n {df_contanenado_ord}')
print(f'Filas de DF ordenado(concatenado): {filasDFORD} \n Columnas de DF ordenado(concatenado): {columnasDFORD}')


#Obteniendo datos estadisticos de los data frames
#el metodo describe() retorna datos estadisticos de archivo como:
"""
Cantidad de filas
Promedio
Nose que estandar
El minimo
El 25% ( y 50%, %75) hasta el MAX
"""

datos_estadisticos = df.describe()
print(f'Mostrando los datos estadisticos del df: \n {datos_estadisticos}\n')

#Accediendo a un elemento en especifico del df con loc()
#el metodo loc() es capaz de acceder al elemento por el numero de la fila del df y el nombre de la columna del df
elemento = df.loc[2,'edad']
print(f'Mostrando un dato especifico del df con loc(): {elemento}\n')

#Accediendo a un elemento en especifico del df con iloc()
#el metodo iloc() accede al elemento por el indice de la fila del df y indice de la columna del df
elemento2 = df.iloc[2,2]
print(f'Mostrando un elemento en especifico del df con iloc(): {elemento2}\n')

#Mostrando todas filas de una columna
nombres = df.loc[:, 'nombre']
print(f'Mostrando las filas en la columna nombre: \n {nombres} \n')
fila3 = df.loc[3, :]
print(f'Mostrando la fila 3: \n {fila3} \n')

#mostrando filas donde la edad sea mayor a 18
mayor_a18 = df.loc[df['edad']>18, :]
print(f'Mostrando solo las filas que son mayores a 18 años: \n {mayor_a18}\n')