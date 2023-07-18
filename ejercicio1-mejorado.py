curso_dalto = 1.5
curso_corto = 2.5
curso_lento = 7
curso_promedio = 4

diferenciaMin = round((curso_corto / curso_dalto) * 10)
diferenciaMax = round((curso_lento / curso_dalto) * 10)
diferenciaPro = round((curso_promedio / curso_dalto) * 10)

print(f'El curso de dalto dura un {diferenciaMin}% menos que el más rápido')
print(f'El curso de dalto dura un {diferenciaMax}% menos que el más lento')
print(f'El curso de dalto dura un {diferenciaPro}% menos que el promedio')

# Cuánto equivale ver una hora del curso dalto en comparación con los otros cursos

print(f'Ver 10 horas del curso de dalto equivale a {round(curso_dalto / curso_promedio * 10)} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {round(curso_promedio / curso_dalto * 10)} del curso de dalto')
