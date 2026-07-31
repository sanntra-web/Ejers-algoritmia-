"""" 
Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, 
aprobó o si debe recuperar. 
Informar un error si el valor de alguna nota no está entre 0 y 10.
· 
·
·
Se promociona cuando las notas de ambos parciales son mayores o 
iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales 
a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4
"""

def aprobo(var1, var2): 

    resultado = ""

    if((var1 > 10 or var1 < 0) or (var2 > 10 or var2 < 0)): 
        resultado = "Numeros invalidos"
    else: 

        if(var1 >= 7 and var2 >= 7): 
             resultado = "Promociono"
        elif(var1 >=4 and var2 >=4): 
             resultado = "Aprobo"
        else: 
             resultado = "Desaprobo"

    return resultado 

nota1 = int(input("nota 1 "))

nota2 = int(input("nota 1 "))


for i in range(5): 
    variable = aprobo(nota1,nota2)

    print(variable)

    nota1 = int(input("nota 1 "))

    nota2 = int(input("nota 1 "))