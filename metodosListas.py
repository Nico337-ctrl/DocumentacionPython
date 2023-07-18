#funcion list, crea una lista 

lista = list(['hola', 'nico', 17, 369])
print(lista)

#metodo len, cuenta la cantidad de elementos de una lista
met_len = len(lista)
print(met_len)


#metodo append, agrega un dato a la lista 
lista.append('aprende')
print(lista)

#metodo insert, agrega un dato a la lista segun el indice dado
lista.insert(2, 'ojeda')
print(lista)

#metodo extend, agrega varios datos a la lista
lista.extend([False, 2023])
print(lista)

#metodo pop, elemina un dato de una lista por el indice de este "lista.pop('ingresa el indice en el que este el dato')"
#para eleminar el ultimo dato de la lista poner "lista.pop(-1)" o "lista.pop(-2)" para eliminar el anteultimo y asi sucesivamente 
lista.pop(4)
print(lista)


#metodo remove, remover un elemento de la lista por su valor
#si no encuentra el valor a remover lanzara un execpion
lista.remove('hola')
lista.remove('nico')
lista.remove('ojeda')
lista.remove('aprende')
lista.remove(False)
print(lista)


#metodo clear, elimina todos los datos de la lista 
#lista.clear()
#print(lista)


#metodo short, ordena los elementos de la lista de manera ascendente 
#este metodo no funciona con cadenas de texto, sin embargo si funciona con datos booleanos
lista.extend([20,30,2,1,7,1500,False,True,0.5])
print(lista)
lista.sort()
print(lista)

#si agregamos este parametro al metodo el orden sera descendente
# "lista.sort(reverse=True)" hara que el orden de los datos sea descendente
lista.sort(reverse=True)
print(lista)


#metodo reverse, invirtiendo los datos de una lista
#lista.reverse()
#print(lista)

