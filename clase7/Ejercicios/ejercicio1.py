#Ejercicio de List Comprehension con range y for 

#Crea un programa que: 
#1. Genere una lista de números del 1 al 10 usando range. 
#2. Cree una nueva lista que contenga el cuadrado de cada número solo si el número es impar.

numeros = list(range(1, 11))

lista_cuadrados = [num**2 for num in numeros if num % 2 != 0]

print('Lista original:', numeros)
print('Cuadrados de impares:', lista_cuadrados)
