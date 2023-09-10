#creando una funcion que sume dos valores
def sumar():
    #colocamos un bucle
    while True:
        #se pide ingresar los numeros 
        a = input('Ingresa numero 1: ')
        b = input('Ingresa numero 2: ')
        #intentando (try) convertir los datos a numero
        try:
            resultado = int(a) + int(b)
        #si lanza una excepcion, pedirle que re ingrese los numeros
        except:
            print('Se te esta pidiendo un numero, ingresaste un valor no valido.')
        #si sale todo bien se finaliza el bucle
        else:
            break
        finally:
            print('Manejo de excepcion finalizado')
    #mostrando el resultado 
    return resultado 


print(sumar())