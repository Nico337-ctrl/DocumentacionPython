#no usando @property
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
#instanciando la clase Persona
juan = Persona('juan', 17)
#accedemos a la propiedad por un get de la clase instanciada
nombre = juan.get_nombre()
#imprimimos la variable que contiene el objeto con el metodo get que nos mostrara el nombre
print(nombre)


#usando @property 
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    #property es un decorador reservado para las clases
    #que convierte la funcion en una propiedad de la clase, aunque el funcionamiento interno identifica que es una funcion
    #tambien property hace que python identifique que es un getter
    #esto sirve para acceder incluso a un dato muy privado

    
    #esto sirve para usar la anotacion del punto para llamar a get_nombre como si fuera una propiedad o un valor, ocultando el nombre real de la variable
    #pasando de a llamar nombre
    @property
    def nombre(self):
        return self._nombre
    
    #creando un decorador que modifica la propiedad anterior
    @nombre.setter
    def nombre(self, nuevo_nombre):
        return self._nombre

    @nombre.deleter
    def nombre(self):
        del self._nombre
    

nicolas = Persona('Nicolas', 17)
nombre = nicolas.nombre
print(nombre)
#usar property evita que podamos modificar el atributo si lo intentamos como en este caso: nicolas.nombre = 'juan', nos lanzara una excepcion mostrandonos que no es un setter
#incluso si intentaramos modificar la propiedad con el nombre de la variable original tampoco permitiria: nicolas._nombre = 'juan'
print('editando el nombre')

#cambiando la propiedad con el decorador setter
nombre = nicolas.nombre = 'ojeda'
print(nombre)

#eliminando la propiedad con el decorador deleter
#del nicolas.nombre



