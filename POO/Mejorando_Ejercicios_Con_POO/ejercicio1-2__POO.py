#creando una clase texto
class Texto:
    def __init__(self, texto):
        self.texto = texto
    def leerTexto(self):
        palabras = list(self.texto.split())
        leer_palabras = len(palabras)

        #velocidad al leer textos
        leer_yo = leer_palabras / 2 
        leer_como_dalto = leer_palabras * 100 //2*1.3/100
        return f"""
        El texto ingresado tiene {leer_palabras} palabras de contenido. \n
        Tardas {leer_yo} segundo en decirlo el texto que has escrito.\n
        Una persona como Dalto lo diria en {leer_como_dalto} segundos en decir lo mismo.\n
        """
        
        



textico = input('Ingresa un texto: ')
usando_texto = Texto(textico)
print(f'{usando_texto.leerTexto()}')