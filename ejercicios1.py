#diferencia en porcentaje entre el curso actual y el mas rapido de los otros cursos, el mas lento y el promedio

curso_dalto = 1.5
curso_corto = 2.5
curso_lento = 7
curso_promedio = 4

diferenciaMin = 100- (curso_dalto / curso_corto *100)
diferenciaMax = 100- (curso_dalto / curso_lento *100)
diferenciaPro = 100- (curso_dalto / curso_promedio*100)
print(f'el curso de dalto dura un {int(diferenciaMin)}% menos que el mas rapido')
print(f'el curso de dalto dura un {int(diferenciaMax)}% menos que el mas lento')
print(f'el curso de dalto dura un {int(diferenciaPro)}% menos que el promedio')


#diferencia de duracion de los crudos

crudo_promedio = 5
crudo_dalto = 3.5

diferenciaCru = 100- (crudo_dalto / crudo_promedio*100)
print(f'la diferencia de crudo del curso de dalto es de {int(diferenciaCru)}% menos que el promedio')

#cuanto equivale el ver una hora del dalto curso con los otros cursos

print(f'ver 10 horas de el curso de dalto equivale {curso_promedio * 100 // curso_dalto /10} horas de otros cursos')
print(f'ver 10 horas de otros cursos equivale a ver {curso_promedio *100 // curso_promedio / 10} del curso de dalto')

