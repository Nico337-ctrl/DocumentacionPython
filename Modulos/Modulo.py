#importando un modulo y asignandole un nombre mSaludar
#el parametro as, permite renombrar un modulo para no tener complicaciones 
#el parametro as tambien permite renombrar funciones importadas de un modulo
#import modulo_saludar as mSaludar
#importando desde un modulo la funcion saludar o mas funciones
#from modulo_saludar import saludar as saludo_formal
#para importar todas las funciones y demas de un modulo usar "*"
#from modulo_saludar import *, como ejemplo, pero es una mala practica

#saludo = saludo_formal('juan')
#print(saludo)



#saludo2 = mSaludar.saludar('pedro')
#print(saludo2)

#al momento de trabajar con modulos importante separar bien las variables de las funciones, las funciones siempre se declaran primero

#accedemos al nombre de este modulo 
#print(mSaludar.__name__)

def saludo_formal(name):
    return print(f'Hola mi estimado {name}, como te encuentras en este dia')

def saludo_raro(name):
    return print(f'klk {name}, te llegas pa juga o klk')

