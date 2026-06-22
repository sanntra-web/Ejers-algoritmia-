""""
Ej.1 Realizar un programa para ingresar desde el teclado un conjunto de números. Al 
finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lec
tura con -1.
"""


primer_valor = -3213421321
ultimo_valor = -3213421321
primer_iteracion = True

var = int(input("ingrese su numero "))
while(var != -1): 

    if(primer_iteracion == True): 
        primer_valor = var
        primer_iteracion = False

    ultimo_valor = var

    var = int(input("ingrese su numero "))

print("primer valor: ", primer_valor, "ultimo valor: ", ultimo_valor)