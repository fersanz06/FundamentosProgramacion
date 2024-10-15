"""
Ejercicio 10:
    Crea un programa que calcule la calificacion final de un alumno
    con los siguientes porcentajes:
    *55% del promedio de sus tres calificaciones parciales.
    *30% de la calificación del examen final.
    *15% de la calificación de un trabajo final.
Entradas: 
    p1: int
    p2: int
    p3: int
    examen: int
    trabajo_final: int
Salidas:
    calificacion_final
"""
p1 = input ("ingresa el valor de P1: ")
p1 = int (p1)
p2 = input ("ingresa el valor de P32: ")
p2 = int (p2)
p3 = input ("ingresa el valor de P3: ")
p3 = int (p3)
examen = input ("ingresa el valor de Exámen")
examen = int (examen)
tf = input ("ingresa el valor de trabajo final: ")
tf = int (tf)
promedio_parcial = (p1 + p2 + p3) / 3
ponderacion_parcial = (promedio_parcial * 0.55)
ponderacion_examen = (examen * 0.30)
ponderacion_tf = (tf * 0.15)
nota_final = (ponderacion_parcial + ponderacion_examen + ponderacion_tf)
print ("La calificacion final es",nota_final)