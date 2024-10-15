#Ejercicio Integrador 

#Desarrolla un programa que haga lo siguiente: 
#1. Usar un bucle for con range para iterar sobre los números del 1 al 20. 
#2. Usar continue para saltar los números divisibles por 3. 
#3. Usar break para detener la iteración si se encuentra un número mayor que 15. 
#4. Crear un set con los números restantes y verificar si algún número es par. 

numeros = set()

for num in range(1, 21):
    if num % 3 == 0:
        continue
    if num > 15:
        break 

    numeros.add(num)

pares = any(num % 2 == 0 for num in numeros)

if pares:
    numeros_pares = [num for num in numeros if num % 2 == 0]

print('Numeros en el set:', numeros)
print('Numeros pares del set:', numeros_pares)
print('¿Alguno es par?', pares)