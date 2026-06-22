"""Ejercicio 4: En el congreso se vota una ley muy importante. Desarrollar un programa que
permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso y si la misma fue aprobada o no"""
votos_a_favor = int(input("Ingrese la cantidad de votos a favor:"))
votos_en_contra = int(input("Ingrese la cantidad de votos en contra:"))
total_votos = votos_a_favor + votos_en_contra
if total_votos > 0:
    porcentaje_a_favor = (votos_a_favor / total_votos) * 100
    porcentaje_en_contra = (votos_en_contra / total_votos) * 100
    print("Porcentaje_a_favor:", porcentaje_a_favor)
    print("Porcentaje_en_contra:", porcentaje_en_contra)
    if votos_a_favor > votos_en_contra:
        print("La ley fue aprobada.")
    else:
        print("La ley no fue aprobada.")

