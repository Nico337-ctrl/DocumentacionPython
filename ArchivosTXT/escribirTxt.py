#el parametro "w" de write siempre sobreescribira el archivo mientras que el metodo "a" agregara el texto que tu le asignes
with open('ArchivosTXT\\archivo2.txt', 'w', encoding='UTF-8') as archivo:
    #usando writelines para agregar texto al archivo
    archivo.writelines(['- ','Nicolas: hola care pan\n', 'Esteban: klk care pan\n'])
    archivo.writelines(['- ', 'Nicolas: te llegas pa un lol o klk \n', 'Esteban: dale pue'])
