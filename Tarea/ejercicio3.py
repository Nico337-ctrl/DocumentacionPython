# Solicitar al usuario ingresar la cantidad de veces que fue ganador, segundo y tercero.
veces_ganador = int(input("Ingrese la cantidad de veces que fue ganador: "))
veces_segundo = int(input("Ingrese la cantidad de veces que fue segundo: "))
veces_tercero = int(input("Ingrese la cantidad de veces que fue tercero: "))

# Calcular el puntaje utilizando la fórmula dada.
puntaje = (veces_ganador ** 3) + (2 * veces_segundo) - (veces_tercero ** 2)

# Imprimir el puntaje del jugador.
print(f"El puntaje del jugador es: {puntaje}")
