"""Leer 10 números enteros e imprimir su promedio, el mayor valor leído y en qué
posición se encontraba. Si se ingresó más de una vez sólo debe informar la primera.
"""
numero_entero = int(input ("ingrese numero: "))
for i in range(0,11):
    print (numero_entero % 10)
