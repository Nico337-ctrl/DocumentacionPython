class Animal:
    def Comer(self):
        print('Comiendo...')

class Mamifero(Animal):
    def Amamantar(self):
        print('Amamantado...')

class Ave(Animal):
    def Volar(self):
        print('Volando...')


class Murcierlago(Mamifero, Ave):
    pass


vampiro = Murcierlago()
vampiro.Volar()
vampiro.Comer()

