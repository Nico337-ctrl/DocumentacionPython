#encapsulamiento 

class Privado:
    def __init__(self):
        #creando atributos muy privados, privados y publicos:
        #el atributo muy privado se caracteriza por tener doble barra al inicio del nombre "__atributo_muy_privado"
        self.__atributo_muy_aprivado = "pepe"
        #el atributo privado se caracteriza por tener una barra al inicio del nombre "_atributo_privado"
        self._atributo_privado = 'juan'
        #el atributo publico se caracteriza por no tener barra al principio del nombre, como si fuera un atributo normal (publico)
        self.atributo_publico = 'carlo'
        #creando una funcion muy privada 
    def __hablar(self):
        print('hola')

objeto = Privado()


#usando un metodo privado, este retornara una excepcion porque a los metodos muy privados no se puede acceder, a los privados y publicos si 
print(objeto.__hablar())
