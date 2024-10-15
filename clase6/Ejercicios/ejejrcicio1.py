#Ejercicio de Sets y for 

#Crea un programa que reciba una lista de números y realice las siguientes operaciones: 
#1. Crear un set a partir de la lista para eliminar duplicados. 
#2. Iterar sobre el set e imprimir cada número. 
#3. Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set.

numeros = [9, 8, 7, 6, 5, 4, 6, 5, 8, 3, 2]
no_duplicados = set(numeros)
print('Lista sin duplicados:', no_duplicados)

print('\n') # solo es para dejar espacios

for numero in no_duplicados:
    print(f'Numero: ',numero)

    valor_dado = 6

numeros_mayores = set()

for numero in no_duplicados:
    if numero > valor_dado:
        numeros_mayores.add(numero)

print('\n') # solo es para dejar espacios

conteo_numeros_mayores = len(numeros_mayores)
print(f'La cantidad de numeros mayores a {valor_dado} es: ',conteo_numeros_mayores)
