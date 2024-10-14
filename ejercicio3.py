"""
Ejercicio 3:
    Crear un programa que pida los catetos de un triangulo 
    rectangulo, calcule su hipotenusa e imprima el resultado.
Entradas:
    Cateto 1: integer
    Cateto 2: integer
Salidas:
    Hipotenusa: integer

"""
cateto1 = input("ingresa el cateto 1: ")
cateto1 = int(cateto1)
cateto2 = input("ingresa el cateto 2: ")
cateto2 = int(cateto2)
hipotenusa = ( cateto1 * cateto1 + cateto2 *cateto2) ** 0.5
print("la hipotenusa del triangulo es:",hipotenusa) 
