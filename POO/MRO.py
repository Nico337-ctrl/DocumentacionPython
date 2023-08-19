#metodo de resoluciond de orden 
#es el orden en que python busca metodos y atributos en las clases


class A:
    def hablar(self):
        print('habla la clase A')
        
class B(A):
    def hablar(self):
        print('habla la clase B')
        
class C(A):
    def hablar(self):
        print('habla la clase C')

class D(B,C):
    def hablar(self):
        print('habla la clase D')


letra = D()

"""Ejemplo sobre el MRO:"""
#al accder a la metodo "hablar" del la clase instanciada D retornara "habla la clase D", ya que siempre se le dara prioridad al metodo que contiene la clase instanciada
#si el metodo de la clase instanciada estuviera vacio (o que contenga el parametro pass) teniendo en cuenta la herencia pasara lo siguiente:
#en este caso la clase "D" hereda de "(B y C)" en ese orden, esto quiere decir que si siguieramos llamando al metodo hablar de la clase instanciada lo siguiente en aparecer seria: "habla la clase B"
#en caso de la clase "B" que es la de donde hereda la clase "D" el metodo "hablar" ahora ya que la clase mostrara lo que esta tiene
#si la clase "B" en su metodo vuelve a estar vacio o tener "pass", lo que se mostrar al llamar el metodo "hablar" sera lo siguiente "(habla desde la clase C)", ya que python sigue el orden en que se heredan las clases y accede a sus metodos mediante esta
#si la clase "C" en su metodo pasa a estar vacio o tener "pass", lo que se mostrara por orden logico es "hablando desde la clase A", ya que por orden en las herencias esta seria a la ultima a que se recorreria por el orden en que esta asignada y desde donde esta hereda sus atributos o en este caso los metodos

letra.hablar()


"""Ejemplo sobre el MRO2:"""

class A:
    def hablar(self):
        print('habla la clase A')
        
class F:
    def hablar(self):
        print('habla la clase F')
        
class B(A):
    def hablar(self):
        print('habla la clase B')

class C(F):
    def hablar(self):
        print('habla la calse C')

class D(B,C):
    def hablar(self):
        print('habla la clase D')

letra2 = D()
letra2.hablar()
        
#accedemos a todas las propiedades del objeto "letra2" ya que este tiene instanciado la clase D que heredad la mayoria de clases
#accedemos a la clase que queremos usar (en este caso "B"), colocamos el metodo y como parametro ponemos el objeto ya instanciado antes con todas las herencias

B.hablar(letra2)



"""Explicacion:"""
#el MRO tambien funciona con ramas, ejemplo: "A le hereda a B"; "B le hereda a D" y "F le hereda a C"; "C le hereda a D"
#esto quiere decir que si el metodo hablar tiene pass en la clase D, se buscara el metodo en la primera herencia de la clase "D", en este caso la primera herencia de "D" es "B", si no llega a encontrar el metodo tomara el esta heredando de "B", tomara el de la clase "A"
#y si a pesar de todo esto no se encontro el metodo buscara la segunda herencia que tiene la clase D, esta seria "C" y pasara lo que paso con la rama de la primera herencia, si no se llegase a encontrar el metodo buscara la clase predecesora de esta y tomara el metodo que esta contiene


#una forma facil de saber el MRO de un objeto es usando el metodo "mro()"

#este metodo muestra el orden en que se encuentran las clases, ademas de orientarnos para saber en que orden python buscara los metodos y las clases que se encuentran heredando 
print(D.mro())

