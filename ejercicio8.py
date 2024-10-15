"""
Ejercicio 8: 
    Crea un programa que calcule el salario de un vendedor tomando en cuenta su
    salario base y el 10% extra que le dan por comision de 3 sus ventas e imprima el 
    resultado.
Entradas: 
    sueldo_base: int
    venta1: int
    venta2: int
    venta3: int
Salidas:
    sueldo: int
"""
sueldo_base = input("Escribe el sueldo base: ")
sueldo_base = int (sueldo_base)
venta1 = input("Escribe el valor de la venta 1: ")
venta1 = int (venta1)
venta2 = input ("Escribe el valor de la venta 2: ")
venta2 = int (venta2)
venta3 = input ("Escribe el valor de la venta 3: ")
venta3 = int (venta3)
total_de_ventas = (venta1 + venta2 + venta3)
comision = (total_de_ventas * 0.10)
sueldo = (sueldo_base + comision)
print ("El sueldo total del vendedor será",sueldo)