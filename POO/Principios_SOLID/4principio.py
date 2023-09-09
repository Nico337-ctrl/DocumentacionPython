from abc import ABC, abstractclassmethod

class Trabajador(ABC):

    @abstractclassmethod
    def trabajar(self):
        pass

class Dormilon(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass


class Comelon(ABC):
    @abstractclassmethod
    def comer(self):
        pass


class humano(Trabajador, Dormilon, Comelon):
    def trabajar(self):
        return f'Estoy trabajando'
    
    def dormir(self):
        return f'Estoy durmiendo'
    
    def Comelon(self):
        return f'Estoy comiendo'
    

class robot(Trabajador):
    def trabajar(self):
        return f'El robot esta trabajando'
    

#usando el 4 principio solid
#la segregacion de interfaz simple, trata de que el usuario no tenga que usar interfaces que no son necesarias para que el pueda realizar una accion
