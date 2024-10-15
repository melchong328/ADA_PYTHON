# Operaciones Básicas con Tuplas 

# Crea una tupla llamada mi_tupla con los siguientes elementos: (5, 10, 15, 20, 25). 
# Usa el método count para contar cuántas veces aparece el número 10 en la tupla. 
# Usa el método index para encontrar la posición del número 20 en la tupla. 
# Muestra los resultados de las operaciones anteriores.

mi_tupla = (5, 10, 15, 20, 25)

conteo_numero = mi_tupla.count(10)
print(f'El numero 10 aparece {conteo_numero} vez en la tupla.')

posicion_de_20 = mi_tupla.index(20)
print(f'El numero 20 se encuentra en la posicion {posicion_de_20} de la tupla.')
