# Manejo de Matrículas en una Tupla 

# Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105). 
# Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla. 
# Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.

matriculas = (101, 102, 103, 104, 105)

conteo_matricula = matriculas.count(102)
print(f'La matricula 102 aparece: {conteo_matricula} vez en la tupla.')


indice_de_104 = matriculas.index(104)
print(f'La matricula 104 aparece en la posicion {conteo_matricula} de la tupla.')