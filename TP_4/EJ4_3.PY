"""Realizar un programa para ingresar desde el teclado un conjunto de números y
mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
con un valor -1."""

conjunto_de_numeros = int(input("ingrese su numero "))
mayor = conjunto_de_numeros
menor = conjunto_de_numeros
numero = int(input("Ingrese un número (-1 para finalizar): "))

while numero != -1:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
        numero = int(input("Ingrese otro número (-1 para terminar): "))
print("El mayor es:", mayor)
print("El menor es:", menor)