#esta es la manera optima de abrir un archivo txt y acceder a el, osea que la manera no optima es la que
#se encuentra en leerTxt.py

#abriendo el archivo con with open()
with open('ArchivosTXT\\hola.txt', encoding='UTF-8') as archivo:

    #mostramos el contenido del archivo
    print(archivo.read())

#con esta funcion no es necesario cerrar el archivo