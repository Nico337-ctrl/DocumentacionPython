        
estudiantes = []
cantidad = int(input('Ingrese la cantidad de estudiantes: '))
for i in range(cantidad):
    nombre = input('Ingresa el nombre del estudiante: ')
    nota1 = float(input(f'Ingresa la nota1 del estudiante {nombre}: '))
    nota2 = float(input(f'Ingresa la nota2 del estudiante {nombre}: '))
    nota3 = float(input(f'Ingresa la nota3 del estudiante {nombre}: '))
    estudiante = (nombre, nota1, nota2, nota3)
    estudiantes.append(estudiante)
for est in estudiantes:
    est[0][1:]
    promedio = float(sum(est)/3)
    print(promedio)
#sancando el promeido
# est = estudiantes[0][1:]
# promedio = sum(est)/3
# print(round(promedio))


