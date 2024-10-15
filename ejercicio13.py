"""
Ejercicio 13:
    Crea un programa que pida al usuario un número, calcule su raíz cuadrada 
    y su raíz cúbica e imprima el resultado.
Entradas: 
    num: int
Salidas:
    raiz_cuadrada: int
    raiz_cubica: int
"""
num = input ("Escribe un número: ")
num = int (num)
raiz_cuadrada = (num ** 1/2)
raiz_cubica = (num ** 1/3)
print ("la raiz cuadrada es",raiz_cuadrada)
print ("la raiz cubica es",raiz_cubica)