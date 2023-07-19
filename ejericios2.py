#1 alumno es profesor
#1 alumno es asistente

#pedir edad de los compañeros de clase que vinieron a clase y ordenar los datos de mayor a menor
#el mayor de la clase es el profesor y el menor de la clase es el asistente
#¿quien es el profesor y quien es el asistente?
"""
respuestas = {}

formulario_activo = True

while formulario_activo:
    nombre = input("\nCual es tu nombre? ")
    respuesta = input(f"Que edad tienes {nombre}? ")

    respuestas[nombre] = respuesta

    pregunta = input("Alguien mas quiere hacer la encuesta? (si/no) ")
    if pregunta == 'no':
        formulario_activo = False

print("\n ----Resultados de la encuesta----")
for nombre, respuesta in respuestas.items():
    print(f"{nombre} hoy {respuesta} te gusto el clima que hizo hoy.")
    

#version 1.2

formActive = True
def realizarEncuesta():
    while formActive:
        nombre = list(input('Ingresa tu nombre: '))
        edad = list(input(f'Ingresa tu edad {nombre}'))

        interrogacion = input('deseas realizar otra vez el formulario?: ')
        if(interrogacion == 'si'):
"""            
#resolviendo el ejercicio 2 con una funcion
#funcion para obtener al asistente y al profesor de la clase seguna la edad:
def generarCompañeros(cantidad):
    #creando una lista de compañeros
    compañeros = []

    #ejecutando un for para pedir los datos de cada compañero
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
asistente, profesor = generarCompañeros(5)

#mostramos el resultado
print(f'el asisente es {asistente} y el profesor es {profesor}')