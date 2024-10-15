# Ejercicio 2: Generador de Números Aleatorios con el Módulo random 
#• Objetivo: Trabajar con funciones de generación de números aleatorios del módulo random. 
#• Descripción: Simula el lanzamiento de un dado y genera una lista de números aleatorios. 
#• Instrucciones: 
#✓ Simula el lanzamiento de un dado de 6 caras (números del 1 al 6) cinco veces. 
#✓ Genera una lista de 10 números aleatorios entre 1 y 100. 
#✓ Selecciona aleatoriamente un número de la lista generada. 


import random


print("Lanzamientos de dado:")
for _ in range(5):
    lanzamiento = random.randint(1, 6)
    print(f"Lanzamiento: {lanzamiento}")

lista_numeros = [random.randint(1, 100) for _ in range(10)]
print("\nLista de números aleatorios:")
print(lista_numeros)


numero_seleccionar = random.choice(lista_numeros)
print(f"\nNúmero seleccionado aleatoriamente de la lista: {numero_seleccionar}")