"""Dados dos parámetros enteros A y B, obtener AB
(A elevado a la B) mediante
multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar. Por ejemplo 43
 = 4 * 4 * 4.
"""
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
def elevar_por_multiplicaciones(a, b):
    resultado = 1

    print("Elevando (a) a la (b) usando multiplicaciones:")
    for i in range(b):
        elevada = (resultado, a)
        print("Multiplicando (resultado) por (a): (resultado) = (resultado / a) * (a) = (resultado)")
    return elevada


