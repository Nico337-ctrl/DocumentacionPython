#creando un guardado de datos en archivos csv con POO
import pandas as pd

datos = {}


class Datos:
    def __init__(self, nombre0, nombre1, apellido0, apellido1, edad, documento):
        self.nombre0 = nombre0
        self.nombre1 = nombre1
        self.apellido0 = apellido0
        self.apellido1 = apellido1
        self.edad = edad
        self.documento  = documento

    def ProcesarDatos(self):
        df = pd.read_csv('POO\\Mejorando_Ejercicios_Con_POO')
        df.writelines(self.nombre, self.nombre1)


        

