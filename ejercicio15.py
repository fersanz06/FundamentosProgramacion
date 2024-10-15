"""
Ejercicio 15:
    Crea un programa que pida dos variables numericas (a y b) al usuario e
    intercambie los valores de ambas variables y muestre cuanto valen al final,
    e imprima el resultado
Entradas: 
    a: int
    b: int
Salidas:
    a: int
    b: int
"""
a = input ("ingresa el valor de a: ")
a = int (a)
b = input ("ingresa el valor de b: ")
b = int (b)
temporal = a
a = b
b = temporal
print ("el nuevo valor de a es: ",a)
print ("el nuevo valor de b es: ",b)