class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return f'estoy volando'
    
class AveNoVoladora(Ave):
    pass


#las subclases que herende de la clase base tienen que poder lo que la clase base haga
#principio de sustitucion de liskov