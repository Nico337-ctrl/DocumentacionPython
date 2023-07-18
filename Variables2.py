#desempaquetado de variables 
#ejemplo con una tupla

tupla = ('perro', 'pato', 100)

animal1,animal2,numero = tupla #ejemplo de desempaquetado
print(numero)


tupla_con_tuple = tuple(['gato', 'michi', 'gagito'])
#las tuplas tambien se pueden crear sin necesidad de "()" de esta forma
tuplas = 'dato1','dato2'



#CONJUNTOS

conjunto = set(['dato1', 'dato2'])
#conjunto_iterable = {['dato', ('dato1', 'dato2')]}

#metiendo un conjunto dentro de otro conjunto
conju = frozenset(['dato1', 'dato2'])
conju2 = {conju, 'dato3'}
print(conju2)


#teorias de conjuntos


met_conju = {1,2,3,4}
met_conju2 = {1,3,4,}

#metodo issubset(), siver para verificar si un subconjunto es el conjunto de otro devolviendo True en caso de ser verdad,
#regresa False de lo contrario, el metodo se usa asi "variable = subconjunto.issubset(conjunto)", dentro de ('se agrega el conjunto a que corresponde el subconjunto')
met_conju_result = met_conju2.issubset(met_conju)
#una forma de hacer este metodo de manera distinta es haciendo esto
#met_conju_result = met_conju2 <= met_conju
print(met_conju_result)


#metodo issuperset(), es lo contrario del metodo 'issubset()', este verifica que un conjunto sea el superconjunto de un conjunto, devuelve True si se cumple la condicion
#regresa False de lo contrario, el metodo se usa asi "variable = superconjunto.issuperset(conjunto)", dentro de ('se agrega el conjunto al que corresponde el superconjunto')
met_conju_result2 = met_conju.issuperset(met_conju2)
#una forma de hacer este metodo de manera distinta es haciendo esto
#met_conju_result = met_conju > met_conju2
print(met_conju_result2)


#metodo isdisjoint(), devolvera True si los conjuntos que estan siendo comparados no tienen ningun dato en comun, devolvera False de lo contrario
met_conju_result3 = met_conju.isdisjoint(met_conju2)
print(met_conju_result3)



