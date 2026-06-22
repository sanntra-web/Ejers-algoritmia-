"""Ejercicio 3: Desarrollar un programa que solicite un número de mes (por ejemplo 4) y
escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y
mostrar un mensaje de error en caso de que no lo sea.
"""
mes = int(input("ingrese el numero del mes:"))
if mes == 1:
    print("Enero")
if mes == 2:
    print("Febrero")
if mes == 3:
    print("Marzo")
if mes == 4:
    print("Abril")
else:
    print("Mes inválido")
