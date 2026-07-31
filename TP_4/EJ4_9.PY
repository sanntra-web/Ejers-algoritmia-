"""Se desea analizar cuántos autos circulan con patente con numeración par y
cuántos con numeración impar en un día. Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe
cuántos vehículos pasaron con numeración par y cuántos con numeración impar."""

par = 0
impar = 0
terminacion = int(input("Ingrese la terminación de la patente (entre 0 y 9) (-1 para finalizar): "))

while terminacion != -1:
    if terminacion % 2 == 0:
        par += 1
    else:
        impar += 1
    terminacion = int(input("Ingrese la terminación de la patente (entre 0 y 9) (-1 para finalizar): "))
print("Vehículos con numeración par: ", par)
print("Vehículos con numeración impar: ", impar)
