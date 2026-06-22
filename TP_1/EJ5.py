"""Ejercicio 5: Calcular el descuento y el importe a pagar por un medicamento adquirido en una
farmacia. El precio del mismo se ingresa por teclado. La farmacia realiza un descuento del 35% a todos los medicamentos. Se solicita mostrar el precio original,
el monto del descuento y el importe final a pagar"""
descuento = 35
importe = int(input("valor de medicamento:"))
print(importe)
print(descuento)
importe_descontado = descuento / 100 * importe
precio_final = (importe - importe_descontado)
print(precio_final)

