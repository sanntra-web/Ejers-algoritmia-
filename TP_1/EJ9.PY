"""Una inmobiliaria paga a sus vendedores un salario de $250000, más una comisión de $50000 por cada venta realizada, más el 5% del valor de las ventas.
Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. 
Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas."""
salario_base = 250000
comision_por_venta = 50000
porcentaje_ventas = 0.05
numero_vendedor = int(input("Ingrese el número del vendedor: "))
cantidad_ventas = int(input("Ingrese la cantidad de ventas realizadas: "))
valor_total_ventas = int(input("Ingrese el valor total de las ventas: "))
salario_comision = comision_por_venta * cantidad_ventas
salario_porcentaje = porcentaje_ventas * valor_total_ventas
salario_total = salario_base + salario_comision + salario_porcentaje
print("Número del vendedor:", numero_vendedor)
print("Salario total:", salario_total)
