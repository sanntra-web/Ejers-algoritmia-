"""Imprimir una columna de asteriscos,
donde su altura se recibe como parámetro."""
def columna(altura):

    for i in range(altura):
        print("*")

altura= int (input("ingrese el numero de altura: "))
columna(altura)
    
