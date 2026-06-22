"""Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
3%, Sindicato: 3%"""

sueldo_basico = int(input("Ingrese el sueldo básico: "))
antiguedad = int(input("Ingrese los años de antigüedad: "))
estado_civil = input("Ingrese el estado civil (soltero/casado): ")

if estado_civil == "soltero":
    aumento = sueldo_basico * 0.05 * antiguedad
else:
    aumento = sueldo_basico * 0.07 * antiguedad

sueldo_bruto = sueldo_basico + aumento

jubilacion = sueldo_bruto * 0.11
obra_social = sueldo_bruto * 0.03
sindicato = sueldo_bruto * 0.03
 
descuentos = jubilacion + obra_social + sindicato

sueldo_neto = sueldo_bruto - descuentos

print("Sueldo bruto:", sueldo_bruto)
print("Descuentos:", descuentos)
print("Sueldo neto:", sueldo_neto)