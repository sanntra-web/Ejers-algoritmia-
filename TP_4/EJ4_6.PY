"""Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el
algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
"""
numero = int(input ("ingrese numero para mostrar la tabla: "))
for i in range(1, 13):
    print (numero * i)
    print (i)