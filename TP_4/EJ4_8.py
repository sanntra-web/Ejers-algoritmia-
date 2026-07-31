"""Ingresar números, hasta que la suma de los números pares supere 100. Mostrar
cuántos números se ingresaron en total.
"""
numero = int(input ("ingrese numero: "))
suma_pares = 0
contador = 0

while suma_pares <= 100:
    if numero % 2 == 0:
        suma_pares += numero
    contador += 1
    numero = int(input("ingrese numero: "))
print(contador)