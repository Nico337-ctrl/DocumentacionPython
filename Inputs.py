#input, pedir dato al usuario
#esta funcion devuelve un dato de tipo 'str'
dato = input('dame tu nombre: ')
print(f'el nombre del usuario es: {dato}')

#funcion int, convierte el dato de una variable en numerico (el dato tiene que ser numerico, "16" -> 16)

numero = input('dame el numero a sumar: ')
numero2 = input('ingresa otro al que sumar con el anterior: ')
suma = int(numero) + int(numero2)
print(f'el resultado de la operacion es: {suma}')
