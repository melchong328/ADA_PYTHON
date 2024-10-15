# Define una lista de números predefinida. 
# Pide al usuario que ingrese el índice de inicio y el índice de fin para 
# la sublista. 
# Usa slicing para obtener la sublista. 
# Suma los elementos de la sublista. 
# Muestra la suma. 

lista_numeros = [10, 20, 30, 40, 50, 60]
print("Lista de numeros ", lista_numeros)

indice_inicio = int(input("Ingrese el índice de inicio de la sublista: "))
indice_final = int(input("Ingrese el índice de fin de la sublista: "))

sublista = lista_numeros[indice_inicio: indice_final]
suma_elementos = sum(sublista)
print("La suma de la sublista es: ", suma_elementos)