"""
Ejercicio 4:
    Crea un programa que haga la suma, resta, multiplicación y divición 
    de 2 números dados por el usuario e imprima el resultado.
Entradas:
    num1: int
    num2: int
Salidas:
    suma: int
    resta: int
    multiplicación: int
    divición: int
"""
numero1 = input ("Escribe el número 1: ")
numero1 = int(numero1)
numero2 = input ("Escribe el número 2: ")
numero2 = int(numero2)
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
divicion = numero1 / numero2
print("La suma de numero 1 y numero 2 es:",suma)
print("La resta de numero1 y numero 2 es:",resta)
print("La multiplicacion de numero 1 y numero 2 es:",multiplicacion)
print("la divicion de numero 1 y numero 2 es:",divicion)