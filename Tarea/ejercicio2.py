# Solicitar al usuario ingresar el monto del préstamo, la tasa de interés anual y el número de años.
monto_prestamo = float(input("Ingrese el monto del préstamo: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
num_anios = int(input("Ingrese el número de años: "))

# Calcular la tasa de interés mensual (r) y el número de pagos mensuales (n).
tasa_interes_mensual = (tasa_interes_anual / 12) / 100
num_pagos_mensuales = num_anios * 12

# Calcular el pago mensual (PP) utilizando la fórmula de amortización de préstamos.
if tasa_interes_mensual == 0:
    pago_mensual = monto_prestamo / num_pagos_mensuales
else:
    pago_mensual = monto_prestamo * (tasa_interes_mensual * (1 + tasa_interes_mensual) ** num_pagos_mensuales) / ((1 + tasa_interes_mensual) ** num_pagos_mensuales - 1)

# Imprimir el pago mensual en un formato legible.
print(f"El pago mensual es: ${pago_mensual:.2f}")
