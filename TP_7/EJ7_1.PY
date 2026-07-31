"""Escribir una función para ingresar desde el teclado una serie de números entre A
y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la función mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
carga se deberá ingresar -1. La función recibe como parámetros los valores de A
y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B."""

def ingresar_numeros_entre_rango(A, B):
    lista = []
    numero = int(input("Ingrese un número (-1 para finalizar): "))
    while numero != -1: 
        if (numero >= A and numero <= B):
            lista.append (numero)
        else: 
            print("error") 
        numero = int(input("Ingrese un número (-1 para finalizar): "))


    return lista
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
serie_de_numeros = ingresar_numeros_entre_rango (a, b) 
print (serie_de_numeros)    