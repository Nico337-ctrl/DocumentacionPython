#mejorando con POO el ejercicio 1 de Curso basico

#creando la clase Curso dalto, donde le ingresaremos multiples datos
class CursoDalto:
    def __init__(self, curso_dalto, curso_corto, curso_largo, curso_promedio, crudo_promedio, crudo_dalto):
        #asignando las propiedades
        self.curso_dalto = curso_dalto
        self.curso_corto = curso_corto
        self.curso_largo = curso_largo
        self.curso_promedio = curso_promedio
        self.crudo_promedio = crudo_promedio
        self.crudo_dalto = crudo_dalto

        #creamos una funcion que compare los cursos
        #para acceder a las propiedades ya asignadas anteriormente en la funcion especial "__init__" usamos el self
    def CompararCursos(self):
        diferenciaMin = 100- (self.curso_dalto / self.curso_corto *100)
        diferenciaMax = 100- (self.curso_dalto / self.curso_largo *100)
        diferenciaPro = 100- (self.curso_dalto / self.curso_promedio*100)
        return f"""
        El curso de dalto dura un {int(diferenciaMin)}% menos que el mas corto\n
        El curso de dalto dura un {int(diferenciaMax)}% menos que el mas largo\n
        El curso de dalto dura un {int(diferenciaPro)}% menos que el promedio\n
        """
    def CompararCrudos(self):

        #para acceder a las propiedades ya asignadas anteriormente en la funcion especial "__init__" usamos el self
        diferencia_crudos = 100- (self.crudo_dalto / self.crudo_promedio*100)
        return f'La diferencia del crudo de dalto es de {int(diferencia_crudos)}% menos que el promedio'

#pidiendo al usuario ingresar los valores        
curso_dalto = float(input('Ingresa la duracion del curso de dalto: '))
curso_corto = float(input('Ingresa la duracion del curso de corto: '))
curso_largo = float(input('Ingresa la duracion del curso de largo: '))
curso_promedio = float(input('Ingresa la duracion del curso promedio: '))

#pidiendo al usuario ingresar los valores
crudo_dalto = float(input('Ingresa la duracion del crudo de dalto: '))
crudo_promedio = float(input('Inggresa la duracion de un crudo promedio: '))

#instanciando la clase
escoger_curso = CursoDalto(curso_dalto, curso_corto, curso_largo, curso_promedio, crudo_promedio, crudo_dalto)
print(f'\n Comparando los cursos: {escoger_curso.CompararCursos()}\n\n')

print(f'Comparando los crudos de los cursos: \n {escoger_curso.CompararCrudos()}\n')
