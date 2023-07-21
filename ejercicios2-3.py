#creando una funcion para realizar la operacacion de fibonacci
def fibonacci(num):
    a,b = 0,1
    lista = []
    for i in range(num):
        if a+b > num:
            return num
        else: 
            lista.append(b)
            a,b = b, a+b
    return lista

resultado = fibonacci(2)
print(resultado)

#esta es una variante simplificada el codigo 
primos_hasta =  lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5)  +1 )), range(2, num)))

print(primos_hasta(15))
"""
#codigo explicado:
primos_hasta es una función lambda que toma un argumento num.
range(2, num) crea una secuencia de números enteros desde 2 hasta el valor de num - 1.
La función filter se utiliza para filtrar los elementos de la secuencia de números creada en el paso anterior, manteniendo solo aquellos que cumplan con una cierta condición.
La función lambda dentro del filter se define como lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)).
En esta función lambda, x representa cada número en la secuencia.
range(2, int(x ** 0.5) + 1) crea una secuencia de números enteros desde 2 hasta la raíz cuadrada de x (inclusiva).
all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) devuelve True si x no es divisible por ningún número en el rango mencionado, es decir, si x es primo. Si x es divisible por algún número en el rango, entonces devuelve False.
En resumen, la función primos_hasta devuelve una lista que contiene todos los números primos desde 2 hasta el número dado num. Cuando se llama con primos_hasta(15), imprimirá la lista de números primos hasta el número 15:
"""