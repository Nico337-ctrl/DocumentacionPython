#metodos de diccionarios

diccionario = {
    'nombre' : 'nicolas',
    'apellido' : 'ojeda',
    'edad' : 17
}

#metodo keys, devuelve las claves de los datos dentro del diccionario
claves = diccionario.keys()
print(claves)

#metodo get, devuelve el valor de una clave del diccionario, no lanza exepciones si no encuentra el valor de la clave
met_get = diccionario.get('edad')
print(met_get)

#metodo pop, elemina clave y valor del diccionario 
met_pop = diccionario.pop('edad')
print(diccionario)
#metodo clear, elimina todos las claves y datos del diccionario
#diccionario.clear()
#print(diccionario)

#metodo items, puede hacer un diccionario iterable
dicc_iterable = diccionario.items()
print(dicc_iterable)