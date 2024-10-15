#Ejercicio de while con Condiciones y Contadores 

#Desarrolla un programa que: 
#1. Use un bucle while para generar números de la serie de Fibonacci. 
#2. Continúe generando números hasta que el número actual sea mayor o igual a 100. 
#3. Imprima la serie de Fibonacci generada.

n1, n2 = 0, 1

fibonacci = [n1]

while n2 < 100:
    fibonacci.append(n2)
    n1, n2 = n2, n1 + n2

print('Serie de Fibonacci generada:', fibonacci)