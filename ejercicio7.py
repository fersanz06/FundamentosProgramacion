"""
Ejercicio 7:
    Crea un programa que reciba una cantidad de minutos y muestre por pantallla
    a cuantas horas y minutos corresponde.
Entradas:
    total_minutos: int
Salidas:
    horas: int
    minutos: int
"""
total_minutos = input ("Ingresa la cantidad de minutos: ")
total_minutos = int (total_minutos)
horas = (total_minutos // 60)
minutos = (total_minutos % 60)
print ("La cantidad equivale a",horas,minutos)