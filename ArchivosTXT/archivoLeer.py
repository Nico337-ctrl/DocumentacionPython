#manera no optima de no abrir un archivo txt
archivo_sin_leer = open('ArchivosTXT\\hola.txt', encoding='UTF-8')

#leer el archivo completo
#los archivos solo pueden leerse una sola vez 
#archivo = archivo_sin_leer.read()

#leer linea por linea del archivo
#lineas = archivo_sin_leer.readlines()


#leer una sola linea del archivo
#readline() sirve para leer una cantidad de caracteres del archivo
#leer_linea = archivo_sin_leer.readline()


#cerrar el archivo

archivo  = archivo_sin_leer.close()
print(archivo)