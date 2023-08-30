#forma no optima para usar decoradores 
# #una funcion especial que decora a otra funcion

# #creamos una funcion que recibe como argumento?¿ una funcion
# def decorador(funcion):
#     #se crea la funcion modificada (funcion_base y se crea funcion_base_decorada)
#     def funcion_modificada():
#         #se puede hacer codigo antes de la funcion para darle mas funcionalidad
#         print('antes de llamar a la funcion')
#         funcion()
#         #tambien se puede agregar codigo despues de ser ejecutada la funcion para dar mas funcionalidad
#         print('despues de llamar a la funcion')
#         #se retorna al funcion modificada (funcion_base_decorada)
#     return funcion_modificada

# #ejemplo de usar una funcion decoradora con una funcion de saludo:
# def saludo():
#     print('hola dalto como estas')

# #para accder a la funcion decoradora asginamos una variable a la funcion decorador y le colocamos como argumento la funcion saludo que ya esta creada
# saludo_modificado = decorador(saludo)
# #le agregamos () a la variable que contiene la funcion decorador para ejecutarla y nos retorne la funcion modificada
# saludo_modificado()

#forma optima de usar decoradores
#creamos una funcion que recibe como argumento?¿ una funcion
def decorador(funcion):
    #se crea la funcion modificada (funcion_base y se crea funcion_base_decorada)
    def funcion_modificada():
        #se puede hacer codigo antes de la funcion para darle mas funcionalidad
        print('antes de llamar a la funcion')
        funcion()
        #tambien se puede agregar codigo despues de ser ejecutada la funcion para dar mas funcionalidad
        print('despues de llamar a la funcion')
        #se retorna al funcion modificada (funcion_base_decorada)
    return funcion_modificada


#creamos la palabra reservada decorador que vendria siendo nuestra funcion decoradora
@decorador
#colocar la palabra reservada encima de la funcion hace referencia a que hace parte de la funcion decorador
def saludo():
    print('hola dalto como estas')

#usamos la funcion saludo 
saludo()