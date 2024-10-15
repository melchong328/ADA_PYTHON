# Ejercicio de while y for 

#Desarrolla un programa que haga lo siguiente: 
#1. Usar un bucle while para pedir al usuario que ingrese números hasta que se ingrese el número 0. 
#2. Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0.

numero_intentos = []

while True:
    numero = int(input('Introduzca el número correcto (del 0 al 10): '))
    if numero == 0:
        print('\nIngresaste el número correcto, felicidades.')
        break
    else:
        print('\nIngresaste el número incorrecto, sigue intentando.')
    
    numero_intentos.append(numero)

suma = 0 
for numero in numero_intentos:
    suma += numero

print(f'La suma de los números ingresados es: {suma}')