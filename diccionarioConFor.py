#recorriendo diccionarios con bucles for in

diccionario = {
    'animal' : 'pato',
    'tipo' : 'terrestre',
    'tamaño' : 17
}

#recorriendo un diccionario para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'{key}: {value}')


#agregando condicional a un bucle y usando la funcion continue para saltar la iteracion de un dato
frutas = ['pera', 'manzana', 'aguacate', 'fresa', 'banano']
verduras = ['tomate', 'cebolla', 'lechuga', 'habichuela', 'zanahoria']

for verdura in verduras:
    if verdura == 'habichuela':
        continue
    print(f'voy a cocinar algo con {verdura}')
else: 
    print('->termino el la lista de verduras\n')

print('.-------------------------.\n')

elim_pera = frutas.remove('pera')
add_pera = frutas.insert(4, 'pera')
#la sentencia break hace que el bucle no se siga ejecutando, los "else" tampoco se ejecutaran
#en cambio sin un break el else se ejecutara, y con "continue" tambien ejecutara el "else"
for fruta in frutas: 
    if fruta == 'pera':
        break
    print(f'me voy a comer una {fruta}')
print('->bucle terminado')
print('.-------------------------.\n')

#usando for in en una sola linea de codigo, se duplican los numeros
numeros = [1,7,8,8,10,2,1]
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)