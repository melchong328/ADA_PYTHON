#Ejercicio Combinado 

#Desarrolla un programa que: 
#1. Genere una lista de números aleatorios entre 1 y 20. 
#2. Usa un bucle for con range para iterar sobre la lista. 
#3. Usar continue para saltar números menores de 10. 
#4. Usar break para detener la iteración si se encuentra un número divisible por 15. 
#5. Imprimir todos los números que cumplen las condiciones. 
#6. Utilizar list comprehension para filtrar los números que no cumplen ninguna condición.

numeros = [1, 3, 6, 7, 3, 5, 9, 11, 18, 14, 20, 11, 17]

print('Lista orignal:', numeros)
numeros_cumplen = []

for i in range(len(numeros)):
    num = numeros[i]

    if num < 10:
        continue

    if num % 15 == 0:
        print(f'Numero divisile por 15 encontrado: {num} Detener iteracion.')
        break
    numeros_cumplen.append(num)

numeros_no_cumplen = [num for num in numeros if num < 10 and num % 15 != 0]

print("\nNúmeros que cumplen las condiciones:", numeros_cumplen)
print("Números que no cumplen ninguna condición:", numeros_no_cumplen)

