class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por email a  {self.usuairo.email}')


class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por sms a  {self.usuairo.sms}')
        
class NotificadoWhastapp(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por whatsapp a  {self.usuairo.whatsapp}')


#segundo principo del metodo solid
#abrir y cerrar principio 
#este principio sirve para que el programa este abierto a agregar nueva funcionalidad pero cerrado a modificaciones
