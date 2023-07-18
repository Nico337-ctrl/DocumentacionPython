#

lista = [4,3,7,10,15]
#funcion max, devuelve el numero mayor de una lista
numeroMayor = max(lista)
print(numeroMayor)

#funcion min, duelve el numero menor de una lista
numeroMenor = min(lista)
print(numeroMenor)

#funcion round, redondea numeros decimales
num = round(12.34234234234, 0)
print(num)

#funcion bool, devuelve False si le ingresamos estos datos = 0, vacio, False, None
#devuelve true si le pasamos un numero distinto a 0, cadena, datos no vacios
resultado_bool = bool(0)
print(resultado_bool)


#funcion all, comprueba que todos los datos sean verdaderos, basandose en la caracteristicas de la funcion anterior (bool)
resultado_all = all(['123', "true"])
print(resultado_all)

#funcion sum, se encarga de sumar todos los datos de una cadena (solo permite datos numericos, de lo contrario lanzara una excepcion)
numeros = [1,1,2,64,65,4,54,65,4,5,6,6,21]
suma = sum(numeros)
print(suma)