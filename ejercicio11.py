"""
Ejercicio 11:
    Crea un programa que pida al usuario dos números y muestre la "distancia" entre ellos (el valor
    absoluto de su diferencia, de modo que el resultado sea siempre positivo)
Entradas: 
    num1: int
    num2: int
Salidas:
    diferencia: int
"""
num1 = input ("Escribe el número 1: ")
num1 = int (num1)
num2 = input ("Escribe el número 2 :")
num2 = int (num2)
diferencia = abs (num1 - num2)
print ("la diferencia entre los numeros es",diferencia)