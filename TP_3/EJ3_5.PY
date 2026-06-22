"""Ejercicio 5: Ingresar las notas de los dos parciales de un alumno e indicar si promocionó,
aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está
entre 0 y 10.
· Se promociona cuando las notas de ambos parciales son mayores o
iguales a 7.
· Se aprueba cuando las notas de ambos parciales son mayores o iguales
a 4.
· Se debe recuperar cuando al menos una de las dos notas es menor a 4"""
Parcial1 = int(input("ingrese nota parcial1:"))
Parcial2 = int(input("ingrese nota parcial2:"))
if((Parcial1 > 10 or Parcial2 < 0) or (Parcial2 > 10 or Parcial1 < 0)):
    print("no se puede ingresar notas invalidas")
else:
    if(Parcial1 >= 7 and Parcial2 >= 7):
        print("promocionó")
    elif(Parcial1 >=4 and Parcial2 >=4):
        print("aprobó")
    else:
       print("desaprobó")


