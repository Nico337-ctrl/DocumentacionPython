class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def MostrarPersona(self):
        print(f'Nombre: {self.nombre}; Edad: {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        #usando el super()
        #super().__init__(nombre, edad)

        #haciendolo como si fuera herencia multiple
        Persona.__init__(self, nombre, edad)
        self.grado = grado
    
    def GradoEstudiante(self):
        print(f'Grado del estudiante {self.nombre}: {self.grado} ')

nombre = input('Ingresar nombre: ')
edad = input('Ingresar edad: ')
grado = input('Ingresar grado: ')

nicolas = Estudiante(nombre,edad, grado) 
nicolas.GradoEstudiante()