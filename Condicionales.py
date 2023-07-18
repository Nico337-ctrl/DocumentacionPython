pan = 30
#if 
#if pan == 15:
    #print("el pan vale 15")
#else: 
    #print("el pan vale mas de 15") 

#else 

#elif 
#ejemplo de if anidados 
ingreso_mensual = 72000
gasto_mensual = 8000
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print('estas en deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('estas bien pa')
    else:
        print('estas gastando mucho')    
elif ingreso_mensual > 1000:
    print('estas bien en latam')
elif ingreso_mensual > 500:
    print('estas bien en argentina')
elif ingreso_mensual > 200:
    print('estas bien en venezuela')
else:
    print('sos pobre')
