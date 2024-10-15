"""
Ejercicio 6:
    Crea un programa que calcule el promedio de 3 numeros dados por 
    el usuario e imprima el resultado.
Entradas:
    num1:int
    num2:int
    num3:int
Salidas:
    Promedio:int
"""
num1 = input ("Ingresa el número 1: ")
num1 = int (num1) 
num2 = input ("Ingresa el número 2: ")
num2 = int (num2)
num3 = input ("Ingresa el número 3: ")
num3 = int (num3)
promedio = (num1 + num2 + num3) / 3
print ("El promedio de los números es",promedio)