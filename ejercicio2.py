"""
Ejercicio 2:
    Crear un programa que calcule el perímetro y área de
    un rectangulo dada su base y altura e imprima el resultado
Entradas: 
    Base: Integer
    Altura: Integer
Salidas:
    área: integer
    perímetro: integer

"""
base = input("ingresa la base: ")
base = int(base)
altura = input("ingresa la altura: ")
altura =int(altura)
area = base * altura
perimetro = (base + altura) * 2
print("El area del rectangulo es",area)
print("El perimetro del rectangulo es",perimetro)
