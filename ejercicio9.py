"""
Ejercicio 9:
    Crea un programa que calcule cuanto deberá pagar el cliente de una 
    tienda, si esta ofrece un descuento del 15% sobre el total de la venta 
    e imprima el resultado.
Entradas:
    precio_total: int
Salidas:
    precio_final: int
"""
precio_total = input ("Escribe el precio total: ")
precio_total = int (precio_total)
descuento = (precio_total * 0.15)
precio_final = (precio_total - descuento)
print ("El precio final será",precio_final)