"""Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es primo o no. 
Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad."""
H = int(input("Ingrese un número natural: "))
es_primo = True
if H <= 1:
    es_primo = False
else:
    for i in range(2, int(H ** 0.5) + 1):
        if H % i == 0:
            es_primo = False
if es_primo:
    print(H, "es un número primo.")
else:
    print(H, "no es un número primo.")