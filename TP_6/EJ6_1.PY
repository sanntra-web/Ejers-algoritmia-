"""Escribir una función que reciba como parámetros dos números enteros. Calcular
y devolver el resultado de la multiplicación de ambos valores utilizando solamente sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 .
"""
def multiplicar_por_sumas(a, b):
    resultado = 0
    
    print("Multiplicando (a) por (b) usando sumas:")
    for i in range(b):
        resultado += a
        print("Sumando", (a), "+", (a), "=", (resultado))
    return resultado    


a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
multiplicar_por_sumas (a, b) 
