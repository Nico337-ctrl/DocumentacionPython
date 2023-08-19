#Herencia simple
class Persona:
    def __init__ (self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

#heredando la clase Persona a la clase Empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #metodo super constructor que permite heredar datos de otra clase y asignar nuevos datos a esta clase hija
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

#roberto = Empleado('Roberto', 43, 'Colombiano', 'Programador', 10000)

#print(roberto.edad)


#Herencia multiple
class Programador:
    def __init__(self, lenguaje):
        self.lenguaje = lenguaje

    def programar(self):
        print(f'Hola, me encuentro programando en {self.lenguaje}')
    
    def mostrar_habilidad(self):
        print('Me encuentro mostrando mi habilidad')


class EmpleadoProgramador(Persona, Programador):
    #colocamos todos los datos que va a heredar esta clase 
    def __init__(self, nombre, edad, nacionalidad, lenguaje, salario, empresa):
        #heredando los datos y haciendo que podamos pedirlos:
        Persona.__init__(self, nombre, edad, nacionalidad)
        Programador.__init__(self, lenguaje)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print(f'Hola me presento mi nombre es {self.nombre}, tengo {self.edad}, soy {self.nacionalidad} y \n trabajo para la empresa {self.empresa}.')

juanito = EmpleadoProgramador('juanito', 43, 'Colombiano', 'Python', 10000, 'Jamar')
juanito.presentarse()
juanito.mostrar_habilidad()
juanito.programar()

#super() sirve para acceder a un metodo que esta creado arriba en el codigo y es heradado a la clase que se instancia ahora
#osea que accede a una clase de base o clase padre, este metodo accede a los metodos de la clase padre que esta heredando a la clase instanciada

#probando si juanito es un objeto de la clase Empleado programador, ademas de mostrar la jerarquia de las clases y las instancias que identifican al objeto
instancia = isinstance(juanito, EmpleadoProgramador)
print(instancia)

#verificando si la clase "Programador" es una sub clase en este caso de la clase "EmpleadoProgramador", esta misma funcion se puede usar para verificar la herencia misma de los datos
no_se = issubclass(Programador, EmpleadoProgramador)
print(no_se)