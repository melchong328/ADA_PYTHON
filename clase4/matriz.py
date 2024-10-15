# Definir una matriz de 3x3
matriz = [
    [1, 2, 3], # fila 0
    [4, 5, 6], # fila 1
    [7, 8, 9]  # final 2 (no se pone la coma ya que es la ultima)
]

# Acceder y mostrar algunos elementos específicos
print("Algunos elementos de la matriz: ")
print("Elementos en la fila 0, columna 0: ", matriz[0][0])
print("Elemento en la fina 1, columna 2: ", matriz[1][2])

# Modificar elementos específicos de la matriz
print("\nModificando elementos especificos: ")
matriz[0][1] = 10 # cambier el elemento de la fila 0 columna 1 a 10
matriz[2][0] = 15 # cambier el elemento de la fila 2 columna 0 a 15
print("Matriz despues de las modoficaciones: ")
print(matriz)

# Acceder a una fila completa
print("\n Accediendo a una fila completa: ")
fila_completa = matriz[1] # Obtener toda fila
print("Fila completa en la posicion 1 ", fila_completa)

# Reemplazar una fila completa
print("\nReemplazando una fila completa: ")
matriz[1] = [20, 21, 22]
print("Matriz despues de reemplazar la fila 1: ")
print(matriz)

# Trabajar con una submatriz (parte de una matriz)
submatriz= [matriz[0][1:3], matriz[1][1:3]] # Extraer submatriz de las columnas 1 a 2 de las filas 0 y 1
print("Submatriz extraida: ", submatriz)

# Mostramos toda la matriz al final 
print("\n Matriz completa al final: ")
print(matriz[0])
print(matriz[1])
print(matriz[2])