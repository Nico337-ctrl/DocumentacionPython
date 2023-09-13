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
        #si lanza una excepcion, pedirle que re-ingrese los numeros 
        # #accediendo a la clase padre de las excepciones
        except Exception as e:
            print('Se te esta pidiendo un numero, ingresaste un valor no valido.')
            print(f'ERROR: {type(e).__name__}') #mostrando el nombre del error
        # except ZeroDivisionError:
        #     print('')

        #si sale todo bien se finaliza el bucle
        else:
            break
        #finally siempre se mostrara
        finally:
            print('Manejo de excepcion finalizado')
    #mostrando el resultado 
    return resultado 


print(sumar())