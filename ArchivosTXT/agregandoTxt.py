#usando el metodo "a" para agregar texto en vez de sobreescribirlo
with open('ArchivosTXT\\archivo2.txt', 'a', encoding='UTF-8') as archivo:
    #usando writelines para agregar texto al archivo
    archivo.writelines(['\n- ','Nicolas: ya estoy entrando care pan\n', 'Esteban: dale pue\n'])
    archivo.writelines(['\n- ', 'Nicolas: ñerda care pan se esta demorando dame 2 \n', 'Esteban: dale te espero'])
     
     #usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.writelines(f'agregando linea {i+1} agregada\n')