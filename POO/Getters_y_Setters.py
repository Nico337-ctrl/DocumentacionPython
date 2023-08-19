#creando una clase con atributos muy privados y usango el metodo get para obtener un atributo de esta
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    #creando la funcion con get para obtener el atributo nombre
    def get__nombre(self):
        return self.__nombre

juanito = Persona('juanito', 27)
nombre = juanito.get__nombre()
print(nombre)

