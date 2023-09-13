# Escribe un programa en Python que solicite al usuario ingresar una temperatura en grados Celsius y luego imprima esa temperatura convertida a grados Fahrenheit y Kelvin. Debes proporcionar tres versiones del programa, cada una utilizando un método diferente para formatear la salida: format(), %(), y f-strings.
# Para convertir de ºC a ºF use la fórmula: ºF = ºC x 1.8 + 32. Para convertir de ºF a ºC use la fórmula: ºC = (ºF-32) ÷ 1.8

#version 1 del codigo 

# Solicitar al usuario ingresar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit y Kelvin
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

# Imprimir la temperatura en grados Fahrenheit y Kelvin utilizando format()
print("Temperatura en grados Fahrenheit: {:.2f}".format(fahrenheit))
print("Temperatura en Kelvin: {:.2f}".format(kelvin))


#vesrsion 2 del codigo usando el %

# Solicitar al usuario ingresar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit y Kelvin
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

# Imprimir la temperatura en grados Fahrenheit y Kelvin utilizando el operador %
print("Temperatura en grados Fahrenheit: %.2f" % fahrenheit)
print("Temperatura en Kelvin: %.2f" % kelvin)


#version 3 del codigo usando f-strings

# Solicitar al usuario ingresar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit y Kelvin
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

# Imprimir la temperatura en grados Fahrenheit y Kelvin utilizando f-strings
print(f"Temperatura en grados Fahrenheit: {fahrenheit:.2f}")
print(f"Temperatura en Kelvin: {kelvin:.2f}")

