#importando paquetes y mostrando la ruta en que estan con print("nombre del paquete".__path__)
from Modulos.Paquetes.saludar_normal import saludar_normal as saludoSimple
from Modulos.Paquetes.saludar_raro import saludar_raro as saludoColeto  
#print(Modulos.Paquetes.__path__)

hola = saludoSimple('juan')
print(hola)

holaRaro = saludoColeto('pedro')
print(holaRaro)
