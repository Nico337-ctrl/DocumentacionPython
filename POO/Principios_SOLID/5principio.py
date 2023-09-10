"Tenemos la forma incorrecta de implementar el 5 principio solid"
# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #aqui va toda la logica para verificar la palabra
#         pass


# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self, texto):
#         #usamos el diccinario para corregir el texto
#         pass

#el 5 principio de solid nos abvierte que una interfaz de alto de nivel no puede depender de una de bajo nivel


"forma correcta de implementar el principio solid en el ejemplo anterior usando clases abstractas"

from abc import ABC, abstractclassmethod


class VerificadorOrtografico(ABC):
    
    @abstractclassmethod
    def verficar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #codigo para verficiar si la palabra se encuentra en el diccionario
        pass
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        pass
    
class CorrectorOrtografico():
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        pass


#el verificador es una clase abstracta tenemos todos los metodos que se necesitan ahi, si llegara a tener mas metodos estaria bien
#estamos tranquilos de podamos seguir usando los mismos metodos que tenga el verificador porque al ser una subclase tendria que poder hacer
#todo lo que la clase base haga (Principio de sustitucion de liskov)