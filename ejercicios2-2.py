#creando una funcion que nos devuelva los numeros primos
#entre el 0 y el argumento que pasemos

#crear una funcion que verifique si un numero es primo
def esPrimo(num):
    #verificamos que el numero pasado no puede dividirse 
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i == 0:
            return False
        #si termina el bucle, significa que no fue divisible entonces es primo
        return True

#creando una funcion que retorne una lista con todos los primos
def primoHasta(num):

    #creando la lista
    primos = []
    for i in range(2,num):

        #verificamos si es primo
        resultado = esPrimo(i)
        
        #en caso de que sea lo agregamos a la lista
        if resultado == True:
            primos.append(i)
    #retornamos la lista
    return primos

#creamos el resultado llamando a la funcion y lo mostramos
resultado = primoHasta(13)
print(resultado)