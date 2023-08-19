import pandas as pd

df = pd.read_csv('ArchivosCSV\\archivo.csv')#, #names=['nombres', 'nombres', 'edades']) 
df.columns.str.strip()
print(f'Primera version del df: \n {df}\n\n Lo que se muestre posteriormente seran cambios realizados al df: \n')

#cambiando el tipo de dato de una columna por str
df['edad'] = df['edad'].astype(int)

#reemplazando los datos de la columna apellido
#df['apellido'].replace('loco', 'maestro', inplace=True)
#print(df['apellido'])


#eliminando listas con datos vacios con el metodo dropna()
#elimina las listas que tengan datos vacios
#el metodo dropna() viene con un parametro prederteminado que elimina las filas, pero agregando el parametro axis='1' podremos eliminar las columnas con datos vacios
#df = df.dropna()
#print(df)

#eliminando listas repetidas con el metodo drop_duplicates()
#elimina las listas repetidas
#df = df.drop_duplicates()
#print(df)


#Guardando los cambios en un archivo csv limpio

df.to_csv('Problemas_Txt_&_Csv\\archivo_limpio.csv')

