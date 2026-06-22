"""Ejercicio 6: Una editorial determina el precio de un libro según la cantidad de páginas que
contiene. El costo básico del libro es de $5000, más $32 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación
debe ser en tela, lo que incrementa el costo en $1200. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en otros $3360. Desarrollar un programa
que calcule el costo de un libro dado el número de páginas.
"""
Costo_basico = 5000
Precio_Pagina = 32
Cantidad_de_paginas = int(input("ingrese_cantidad_de_paginas:"))
Costo_total = Costo_basico + (Cantidad_de_paginas * Precio_Pagina)
if Cantidad_de_paginas > 300:
    Costo_total += 1200
    print("Costo final:", Costo_total)
if Cantidad_de_paginas > 600:
    Costo_total += 3360
    print("Costo final:", Costo_total)
else:
    print(Costo_total)