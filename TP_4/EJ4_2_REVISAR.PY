"""Realizar un programa para ingresar desde el teclado un conjunto de números e
informar si la cantidad de elementos es impar o par, sin utilizar contadores. Finalizar la lectura de datos con -1. """

par = True
numero = int(input("Ingrese un número (-1 para finalizar): "))

while numero != -1:
    par = not par
    numero = int(input("Ingrese un número (-1 para finalizar): "))
if par:
    print("La cantidad de elementos es par.")
else:
    print("La cantidad de elementos es impar.")