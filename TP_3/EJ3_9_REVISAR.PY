"""Leer tres números correspondientes al día, mes y año de una fecha e imprimir
un mensaje indicando si la fecha es válida o no."""

anio = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el día: "))
if anio <= 0:
    print("Fecha inválida")
elif mes < 1 or mes > 12:
    print("Fecha inválida")
else:
    if dia >= 1 and dia <= 31:
        print("Fecha válida")
    else:
        print("Fecha inválida")

dia = int(input())
mes = int(input())
anio = int(input())

if((anio < 0) or (dia > 31 or dia < 1) or (mes > 12 or mes <1)): 
    print("fecha es invalida")

else: 
    print("fecha valida")