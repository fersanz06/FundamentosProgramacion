"""
Ejercicio 5:
    Crea un programa que convierta el valor dado en grados Fahrenheit
    a grados Celcius e imprima el resultado
Entradas:
    fahrenheit: int
Salidas:
    celcius: int
"""
fahrenheit = input ("escribe el valor de fahrenheit: ")
fahrenheit = int (fahrenheit)
celcius = (fahrenheit - 32) * 0.5556
print("El valor en celcius es",celcius)