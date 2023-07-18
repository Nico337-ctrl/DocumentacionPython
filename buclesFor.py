#creando bucles con for in
#se pueden iterar tuplas y listas con for in 

animales = ['perro','gato','pez','michi']

#recorriendo la lista animales
for animal in animales:
    print(animal)


#recorriendo la lista de numeros
numeros = [1,2,3,4,5,]
for numero in numeros:
    resultado = numero +2
    print(resultado)

#recorriendo dos listas del mismo tamaño
for numero, animal in zip(numeros, animales):
    print(f'numero: {numero}')
    print(f'animal: {animal}')


#funcion range, le asignas dos parametros: en el que comienza y en el cual termina, algo asi "for contar in range(0,11) en este caso mostrara todos los numeros
#encuentran entre 0 y 11, contanto el 0 y llegando hasta el 10"
#for numero in range(1,10):
#    print(numero)

#si le asignamos solo un paramentro recorrera desde el cero hasta ese numero "for contar in range(10)" 

for contar in range(10):
    print(contar)


#forma optima de recorre una lista con su indice
#funcion enumerate(), 
for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    print(f'indice: {indice} -> valor: {valor}')


#ejercicio de desempaquetado 
flores = ['rosa', 'tulipan', 'lirio', 'margarita']

for flor in flores:
    print(flor)
else: 
    print('se terminaron las flores')

   
