
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print('Estudiando...')

#haciendo que el usuario pueda interactuar con el objeto asignandole los datos
nombre = input('Ingresa tu nombre: ')
edad = input('Ingresa tu edad: ')
grado = input('Ingresa tu grado: ')

#instanciamos la clase
estudiante = Estudiante(nombre, edad, grado)

#mostramos los datos del objeto
print(f"""DATOS DEL ESTUDIANTE: \n\n
    Nombre: {estudiante.nombre} \n
    Edad: {estudiante.edad} \n
    Grado: {estudiante.grado} \n
      """)

#

while True:
    accion = input()
    if accion == 'estudiar':
        estudiante.estudiar()
        break

