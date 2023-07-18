#creando un diccionario con dict()

diccionario = dict(nombre='nicolas', juego='brawlhalla')
print(diccionario)

#las listas no pueden ser claves, usar frozenset para agregar conjuntos a diccionarios,
#las tuplas pueden ser claves en diccionarios diccionario = {('aqui adentor va la tupla dentro de parentensis') : 'y por fuera la clave'}

dicc_tupla = {('tupla', 'tuples') : 'hola'}
print(dicc_tupla)

#creando un diccinario con claves definidias pero sin valores, "dict.fromkeys([])"
dicc_from = dict.fromkeys(["nombre", 'apellido'])
dicc_from2 = dict.fromkeys(['nombre', 'apellido'], 'Nicolas')
print(dicc_from)
print(dicc_from2)