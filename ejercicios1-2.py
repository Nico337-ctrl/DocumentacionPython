texto = input('ingresa un texto: ')

lista = list(texto.split())
leer_lista = len(lista)
print(f'el texto ingresado tiene {leer_lista} palabras de contenido')


leer_texto = leer_lista / 2 # cada 1 segundo 2 palabras
leercomoDalto = leer_lista *100 // 2*1.3 /100 
print(f'tardas {leer_texto} segundos en decir el texto escrito')
print(f'Dalto tarda {leercomoDalto} segundos en decir el mismo texto')

if leer_lista > 120:
    print('tampoco te pedi un textamento')
