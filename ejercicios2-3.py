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

