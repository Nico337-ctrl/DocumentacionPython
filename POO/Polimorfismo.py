
#Polimorfismo 


class gato():
    def sonido(self):
        return 'Miau'


class perro():
    def sonido(self):
        return 'Guau'
    
def hacer_sonido(animal):
    print(animal.sonido())

gato = gato()
perro = perro()
hacer_sonido(gato)

    