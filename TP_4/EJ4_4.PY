"""Ejercicio 4: Desarrollar un programa que imprima la suma
de los números impares comprendidos entre 42 y 176."""

suma = 0
for Y in range(42, 176):
    if Y % 2 != 0:
        suma += Y
print (suma)
print (Y)


