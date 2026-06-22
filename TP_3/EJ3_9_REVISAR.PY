"""Leer tres números correspondientes al día, mes y año de una fecha e imprimir
un mensaje indicando si la fecha es válida o no."""

año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el día: "))
if año <= 0:
    print("Fecha inválida")
elif mes < 1 or mes > 12:
    print("Fecha inválida")
elif mes > 1 and mes < 12:
        print("Fecha válida")
else:
    if dia >= 1 and dia <= 31:
        print("Fecha válida")
    else:
        print("Fecha inválida")