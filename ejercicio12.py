"""
Ejercicio 12: 
    Crea un programa que pida al usuario dos pares de números x1,y2 y x2,y2, 
    que representen dos puntos en el plano y calcula la distancia entre ellos 
    e imprima el resultado.
Entradas:
    x1: int
    y1: int
    x2: int
    y2: int
Salidas:
    distancia: int
"""
x1 = input ("Ingresa el valor de x1: ")
x1 = int (x1)
y1 = input ("Ingresa el valor de y1: ")
y1 = int (y1)
x2 = input ("Ingresa el valor de x2: ")
x2 = int (x2)
y2 = input ("Ingresa el valor de y2: ")
y2 = int (y2)
distancia = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
print ("La distancia de los numeros es",distancia)