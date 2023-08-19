#creando una funcion sin parametros 
def saludando():
    print('hola como estas')

saludando()
print('\n.--------------------------.\n')

#creando funciones con parametros 

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == 'mujer'):
        adjetivo = 'mi reina'
    elif(sexo == 'hombre'):
        adjetivo == 'mi rey'
    else:
        adjetivo == 'mi amor'
    print(f'hola {nombre}, {adjetivo} como estas?')


saludar('camila','mujer')
print('\n.-----------------------------------------.\n')

#usando input en las funciones
"""
def pedirDatos():
    nombre = input('Ingrese su nombre: ')
    edad = input('Ingrese su edad: ')
    sexo = input('Ingrese el sexo con el que se idenfica (hombre/mujer/ninguno): ')
    sexo = sexo.lower()
    if(sexo == 'mujer'):
        adjetivo = 'mi señora'
    elif(sexo == 'hombre'):
        adjetivo = 'mi señor'
    elif(sexo == 'ninguno'):
        adjetivo = ''
    else:
        adjetivo = ''
    print(f'Bienvenido {adjetivo} {nombre}, tienes {edad} años de edad')

pedirDatos()
"""
print('Este codigo se encuentra comentado')
print('\n.---------------------------------.\n')

#creando una funcion para generar contraseñas random 
def genContraseña():
    chars = 'asdfghjklñqwertyuiopzxcvbnm'
    numero = input('ingrese un numero: ')
    numeroEntero = str(numero)
    numero = int(numeroEntero[0])
    c1 = numero -2
    c2 = numero 
    c3 = numero -5
    c4 = numero +3
    c5 = numero +1
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{numero*2}'
    return contraseña, numero

#desempaquetando datos de una funcion
mostrarContraseña, num = genContraseña()
print(f'mostrando tu contraseña: {mostrarContraseña}')
print(f'el numero con que fue generada esta contraseña es: {num}')
print('\n.---------------------------------.\n')


#definiendo una funcion con el parametro args "*"
def sumarValores(nombre,*numeros):
    return f'{nombre} el resultado de la suma optima es: {sum(numeros)}'

resultado = sumarValores('Nicolas',5,12,4,8,4,12)
print(resultado)
print('\n.---------------------------------.\n')

#definiendo una funcion no optima de sumar valores (usando listas)
def sumarNumeros(numeros):
    numerosSumados = 0
    for numero in numeros:
        numerosSumados = numerosSumados + numero
    return numerosSumados

resultadoSuma = sumarNumeros([5,5,5,5,5,5])
print(f'resultado de la suma no optima de valores: {resultadoSuma}')
print('\n.---------------------------------.\n')


#definiendo una funcion y ingresando parametros posicionales de la funcion 

def datos(nombre, apellido, adjetivo):
    return f'hola {nombre} {apellido}, eres muy {adjetivo}'

#utilizando keywrods arguments
frase = datos(adjetivo='capo', nombre='nicolas', apellido='ojeda')
print(frase)
print('\n.---------------------------------.\n')

#creando una funcion con un parametro opcional y uno por defecto
#el parametro por defecto se asigna directamente en la funcion 
#el parametro opcional se asigna cuando llamamos a la funcion 
#en este caso el parametro por defecto es la variable adjetivo y se le asigna un parametro opcional reemplazando el por defecto cuando se llamda a la funcion
def datos2(nombre, apellido, adjetivo = 'capo'):
    return f'hola {nombre} {apellido}, eres muy {adjetivo}'

frase2 = datos(adjetivo='inteligente', nombre='nicolas', apellido='ojeda')
print(frase2)
print('\n.---------------------------------.\n')


#creando una funcion que idenfique numeros pares
def numerosPares(numero):
    if(numero %2 == 0):
        return True
    
lista = ['1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17']
numeros_pares = filter(numerosPares, lista)

print(list(numeros_pares))