#metodos especiales, son funciones reservadas de python para realizar ciertas acciones que no podriamos hacer como metodos normales

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #el metodo especial "__str__" permite mostrar como se veria representado la instancia de una clase
    #si fuera una cadena de texto, cuando se llame al objeto se motrara lo que retorne la funcion con este metodo especial
    def __str__(self):
        return f'Persona(nombre=({self.nombre}),edad=({self.edad}))'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",({self.edad}))'
    
    #el metodo especial "__add__" permite definir la suma de las clases 
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)

juan = Persona('Juan', 5)

camilo = Persona('camilo', 7)
pedro = Persona('pedro', 3)
nueva_persona = juan + camilo + pedro 
print(nueva_persona.nombre)

#otros metodos especiales

