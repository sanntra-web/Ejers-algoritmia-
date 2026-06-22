"""El factorial de un número entero N mayor que cero se define como el producto
de todos los enteros X tales que 0 < X <= N. Desarrollar un programa para calcular el factorial de un número dado. Deberán rechazarse las entradas inválidas
(menores que 0)"""
N = int(input("Ingrese un número entero mayor que cero: "))
if N < 0:
    print("Entrada inválida. Por favor, ingrese un número entero mayor que cero.")
else:
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    print("El factorial de N es:" + str(factorial))