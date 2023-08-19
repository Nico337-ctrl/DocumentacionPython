#creando una clase temporal 
class Celular:
    #__init__ como metodo especial y asginandole el parametro self, para hacer referencia a asi mismo
    #esta funcion se ejecutara al momento de instanciar la clase
    #esto es una funcion constructora o metodo constuctor
    def __init__(self, marca, modelo, camara):
        #escribir "self.marca" es igual a decir "celular.marca"
        #agregando propiedades con "self" y se le agrega la propiedad o atributo como si fuera un metodo y se le asigna una variable que contendra el dato que le pasemos al instanciar la clase
        self.marca = marca
        #self hace referencia al objeto y la propiedad que este tendra y luego se le asigna el dato que le pasamos al instanciar la clase
        #cabe resalta que la palabra que esta junto a self (modelo) no es la misma a la que se le asigna luego, actuan de manera diferente
        self.modelo = modelo
        self.camara = camara
        
#instanciamos la clase 
celular1 = Celular('samsung', 'S23', '48MP')
print(celular1.marca)

#instaciamos la clase otra vez
celular2 = Celular('Iphone', '15 PRO', '100MP')
print(celular2.marca)


#creando una clase con nombres de propiedades diferentes
#self.pepe es el nombre de la propiedad a la cual se puede acceder
#sefl.pepe = marca es la variable a la que sera igual esta propiedad, osea, que para acceder a esta propiedad no podemos hacer esto "print(objeto.marca)", porque nos retornara un error porque no se encontro la propiedad marca
#para evitar este error tendriamos que hacer esto "print(objeto.pepe)" y ahora si mostrara la marca, osea "oppo" que es lo que contiene la variable marca
class Celulares:
    def __init__(self, marca, modelo, camara):
        self.pepe = marca
        self.pan = modelo
        self.agua = camara

#instanciando la clase con nombres de propiedades diferentes a los argumentos que se le asignan a la clase
objeto = Celulares('oppo', 'i43', '30mp')
print(objeto.pepe)