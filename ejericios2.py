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
def generarCompañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input('Ingresa tu nombre: ')
        edad = int(input('Ingresa tu edad: '))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor


asistente, profesor = generarCompañeros(5)
print(f'el asisente es {asistente} y el profesor es {profesor}')