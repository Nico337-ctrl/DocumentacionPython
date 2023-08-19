class Celular:
    #__init__ como metodo especial y asginandole el parametro self, para hacer referencia a asi mismo
    #esta funcion se ejecutara al momento de instanciar la clase
    #esto es una funcion constructora o metodo constuctor
    def __init__(self, marca, modelo, numero):
        #escribir "self.marca" es igual a decir "celular.marca"
        #agregando propiedades con "self" y se le agrega la propiedad o atributo como si fuera un metodo y se le asigna una variable que contendra el dato que le pasemos al instanciar la clase
        self.marca = marca
        #self hace referencia al objeto y la propiedad que este tendra y luego se le asigna el dato que le pasamos al instanciar la clase
        #cabe resalta que la palabra que esta junto a self (modelo) no es la misma a la que se le asigna luego, actuan de manera diferente
        self.modelo = modelo
        self.numero = numero

    #toda funcion dentro de una clase pasa a llamarse metodo y tenemos que asignarle el parametro self para que el objeto pueda usar la anotacion del punto y usar este metodo
    def Llamar(self):
        #accedemos a la propiedad de la clase con "self"
        print(f'estas llamando desde tu: {self.numero} ')

    def Colgar(self):
        #accedemos a la propiedad de la clase con "self"
        print(f'estas colgando desde tu: {self.numero} ')

#instanciamos al clase
miCelular = Celular('Samsung', 'S23', '3145271623')

#accedemos al metodo llamar de la clase Celular
miCelular.Llamar()
