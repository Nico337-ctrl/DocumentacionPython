"""class compañeros:
    def __init__(self, nombre, edad):
        compañeros = []
        self.nombre = nombre
        self.edad = edad
        compañero = self.nombre, self.edad

        compañeros.append(compañero)

for i in range(cantidad):
    nombre = input('Ingresa tu nombre: ')
    edad = int(input('Ingresa tu edad: '))
    compañero = (nombre, edad)
        
    #agregando la informacion a la lista
        compañeros.append(compañero)

        #ordenando de mayor a menor segun la edad
        compañeros.sort(key=lambda x:x[1])

        #compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre para definir al asistente y el profesor 
        asistente = compañeros[0][0]
        profesor = compañeros[-1][0]

        #retornamos una tupla
        return asistente, profesor


#desempaquetamos lo que retorna la funcion 
compañeross = compañeros()

asistente, profesor = compañeros.generarCompañeros(5)

#mostramos el resultado
print(f'el asisente es {compañeros.asistente} y el profesor es {compañeros.profesor}')
"""

class Compañeros:
    def __init__(self, nombre, edad, cantidad):
        self.cantida = cantidad
        self.nombre = nombre
        self.edad = edad

    def elegirA_P(self):
        compañeros = []
        compañero = (self.nombre, self.edad)
        compañeros.append(compañero)

        compañeros.sort(key=lambda x:x[1])
        asistente = compañeros[0][0]
        profesor = compañeros[-1][0]

        return f'el asistente es: {asistente} y el profesor es: {profesor}.'


cantidad = int(input('Ingresa la cantidad de compis: '))

for i in range(cantidad):    
    nombre = input('Ingres tu nombre compita: ')
    edad = int(input('Ingresa tu edad compita: '))
compitas = Compañeros(nombre, edad, cantidad)
print(f'{compitas.elegirA_P()}')