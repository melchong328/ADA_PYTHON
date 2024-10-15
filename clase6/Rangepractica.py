# range() : crea una lista inmutable de numeros enteros en sucesion aritmetica.

numeros = range(5) # [0, 1, 2, 3, 4]

print(numeros[1])

numeros1 = range(4, 10) # [4, 5, 6, 7, 8, 9]
                        #  0  1  2 3
print(numeros1[3])

numeros2 = range(10, 100, 8) # inicia del 10 y termina antes del 100 y va de 8 en 8
print(numeros2[9]) # [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98]