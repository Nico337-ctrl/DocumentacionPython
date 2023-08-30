#el juego consiste en crear personajes un juego y que esos personajes se puedan fusionar
#para formar personajes mas poderosos que tengan mas poder
#para ello cambiar el comportamiento del operador "+" para cuando los personajes se fucionen creen uno con sus habilidades se eleven al cuadrado

class Personaje:
    def __init__(self, nombre, fuerza, poder):
        self.nombre = nombre
        self.fuerza = fuerza
        self.poder = poder
    def __repr__(self):
        return f'{self.nombre} fuerza: {self.fuerza} poder: {self.poder}'
    def __add__(self, otroPJ):
        nuevo_PJ = self.nombre + "-" + otroPJ.nombre
        nuevo_FZ = round(((self.fuerza + otroPJ.fuerza)/2)**1.5)
        nuevo_PW = round(((self.poder + otroPJ.poder)/2)**1.5)
        return Personaje(nuevo_PJ, nuevo_FZ, nuevo_PW)
    

goku = Personaje('Goku', 100, 150)
vegeta = Personaje('Vegeta', 80, 120)

gogeta = goku + vegeta
print(gogeta)