# Ejercicio 1: Operaciones Matemáticas con el Módulo math 
# • Objetivo: Practicar con las funciones matemáticas básicas del módulo math. 
# • Descripción: Utiliza las funciones del módulo math para realizar  operaciones matemáticas avanzadas. 
#• Instrucciones: Solicita al usuario que ingrese un número decimal. 
#Usa las siguientes funciones del módulo math para realizar diferentes cálculos: 
#✓ math.ceil(): Redondear al entero superior. 
#✓ math.floor(): Redondear al entero inferior. 
#✓ math.sqrt(): Obtener la raíz cuadrada. 
#✓ math.factorial(): Calcular el factorial (solo si es un número entero no negativo). 
#✓ math.pow(): Elevar el número a la potencia de otro número.

import math

numero = float(input("Ingrese un número: "))

# operacioness
print(f"\nOperaciones con {numero}:")
print(f"Redondeo hacia arriba: {math.ceil(numero)}")
print(f"Redondeo hacia abajo: {math.floor(numero)}")
print(f"Raíz cuadrada: {math.sqrt(numero)}")


if numero.is_integer() and numero >= 0:
    print(f"Factorial: {math.factorial(int(numero))}")
else:
    print("Factorial: No aplicable")


exponente = float(input("Ingrese el exponente para la potencia: "))
print(f"{numero} elevado a {exponente}: {math.pow(numero, exponente)}")