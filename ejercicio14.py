"""
Ejercicio 14:
    Crea un programa que pida un número de dos cifras al usuario, y que permita 
    obtener el número invertido.
Entradas:
    num: int
Salidas:
    num_invertido: int
"""
num = input ("Ingresa un número de 2 digitos: ")
num = int (num)
decenas = (num // 10)
unidades = (num % 10)
num_invertido = ((unidades * 10) + decenas)
print ("El número invertido es",num_invertido)