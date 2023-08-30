#la abstraccion en concepto de POO es ocultar la complejidad interna de un sistema 
#y mostrar solo lo requerido y funcional para usarlo


#la abstraccion en un termino tecnico seria las clases abstractas y lo que contrae
from abc import ABC, abstractclassmethod
#creando una clase abstracta
class Persona(ABC):
    #agregando un metodo abstracto
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    #este metodo no es necesario que sea abstracto ya que este lo puede hacer cualquier persona (persona es la clase abstracta)
    def presentarse(self):
        print(f'Hola me llamo: {self.nombre} y tengo {self.edad} años')


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'estoy trabando en el area de: {self.actividad}')


Nicolas = Trabajador('Nicolas', 18, 'Masculino', 'programacion')
Miguel = Estudiante('Miguel', 18, 'Masculino', 'cocina')

Nicolas.presentarse()
Nicolas.hacer_actividad()
Miguel.presentarse()
Miguel.hacer_actividad()