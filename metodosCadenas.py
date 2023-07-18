txt = "HOLA GATO"
#funcion dir muestra todo lo que se puede hacer con una cadena
print('metodo dir:')
print(dir(txt))

#upper 

txt2 = "hola michi"
resultado = txt2.upper()
#metodo upper convierte una cadena a mayusculas 
print(f'metodo upper: {resultado}')

#metodo lower convierte una cadena en minusculas
resultado2 = txt.lower()
print(f'metodo lower: {resultado2}')


#metodo captalize convierte la primera letra en mayuscula de la cadena 
resultado3 = txt2.capitalize()
print(f'metodo captalize: {resultado3}')

#metodo find busca una cadena en una cadena, si no hay coindencias devuelve -1
busqueda_find = txt.find('H')
print(busqueda_find)

#metodo index busca una cadena dentro de una cadena, si no hay coincidencias devuelve una excepcion
# es sensible a mayusculas y minusculas 
busqueda_index = txt.index('A')
print(busqueda_index)


#metodo isnumeric, si es numerico regresa true de lo contrario regresa false
es_numerico = txt.isnumeric()
print(es_numerico)

#metodo isalpha, si es alfa numerico regresa true, si no regresa false
#es sencible a los espacios, signos y numeros
es_alfanumerico = txt.isalpha()
print(es_alfanumerico)

#metodo count, devuelve el numero de ocurrencias de una subcadena en una cadena, regresa 0 si no encontro la cadena
#es sensible a espaciados 
busqueda_count = txt.count('A')
print(busqueda_count)

#funcion len, cuenta cuantos caracteres tiene una cadena
#incluye los espacios como caracteres
busqueda_len = len(txt)
print(busqueda_len)

#metodo startwith, verifica si una cadena empieza con la cadena dada si es asi devuelve true, de lo contrario devuelve false
#es sensible a mayusculas y minusculas
busqueda_startwith = txt.startswith('H')
print(busqueda_startwith)

#metodo endswith, verifica si una cadena empieza con la cadena dad si es asi devuelve true, de lo contrario devuelve false
busqueda_endswith = txt.endswith('O')
print(busqueda_endswith)

#metodo replace, reemplaza un trozo de la cadena dada por otra otorgada
#en caso de no encontrar coincidencias con la primera cadena dada, regresara la cadena anterior y no realizara cambios
reemplazar = txt.replace('HOLA', 'Hola')
print(reemplazar)

#metodo SPLIT
#separar cadenas con la cadena que le demos
cadena_split = txt.split(' ')
print(cadena_split)
print(type(cadena_split))