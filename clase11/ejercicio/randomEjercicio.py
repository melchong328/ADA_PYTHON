import random

# Generar un numero flotante aleatorio entre 0 y 1
numero_aleatorio = random.random()
print(f'Numero aleatorio (0-1): {numero_aleatorio}')

# Generar un numero entero aleatorio entre 1 y 10
numero_entero = random.radiant(1, 10)
print(f'Numero entero aleatorio (1-10): {numero_entero}')

# Seleccionar una fruta al azar de una lista
fruta = ['manzana', 'naranja', 'banana', 'uva', 'pera']
fruta_elegida = random.choice(fruta)
print(f'Fruta elegida: {fruta_elegida}')

# Mezclar aleatoriamente una lista de numeros
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f'Numeros mezclados: {numeros}')

