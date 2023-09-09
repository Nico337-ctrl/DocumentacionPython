class TanqueCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible 
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print('El auto se ha movido')
        else:
            print('No hay sufienciente combustible')

    def obtener_posicion(self):
        return self.posicion
    

tanque = TanqueCombustible()
toyota = Auto(tanque)


print(toyota.obtener_posicion())
toyota.mover(15)
print(toyota.obtener_posicion())
toyota.mover(15)
print(toyota.obtener_posicion())
toyota.mover(15)


#experimentando con el primer principo de solid
#principio de responsabilidad unica
