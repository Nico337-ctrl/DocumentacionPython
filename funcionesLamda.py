#creando funciones anonimas con lamda
#las funciones lambda sirven para hacer cosas sencillas y rapidas
#retornan valores automaticamente
#no son aptas para realizar mas de una instruccion
multiplicar = lambda x : x*2

#creando una funcion lambda para identificar numeros pares
numeros = [1,2,3,4,5,6,7,8,9]
numerosPares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numerosPares))

