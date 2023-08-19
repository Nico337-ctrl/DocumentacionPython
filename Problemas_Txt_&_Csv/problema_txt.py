nombres = ['nicolas', 'pedro', 'camilo', 'victor']
apellidos = ['ojeda', 'perez', 'vanegas', 'osorio']

with open('Problemas Txt y Csv\\nombresYapellidos.txt', 'w') as archivo:
    archivo.writelines('Los datos son: \n')
    [archivo.writelines(f'Nombre: {n}\n Apellido: {a}\n............\n')for n,a in zip(nombres, apellidos)]