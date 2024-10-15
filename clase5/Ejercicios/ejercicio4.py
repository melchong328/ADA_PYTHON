# Lista de Diccionarios 

#1. Crea una lista de diccionarios, donde cada diccionario representa un estudiante con las siguientes claves: 
# o Nombre 
#o Edad 
#o Calificaciones (que es una lista de números) 
#2. Imprime el nombre y las calificaciones del primer estudiante en la lista.

Estudiantes= [{
    "Nombre": "Mar",
    "Edad" : 24,
    "Calificaciones" : [10, 9, 8, 8]}, 
    {"Nombre": "Richard",
    "Edad" : 25,
    "Calificaciones" : [7, 8, 7, 9]},
    {"Nombre": "Katia",
    "Edad" : 24,
    "Calificaciones" : [10, 10, 8, 9]},
    {"Nombre": "Daniel",
    "Edad" : 26,
    "Calificaciones" : [10, 6, 7, 8]}]

estudiante_uno = Estudiantes[0]
print("Nombre del primer estudiante: ", estudiante_uno["Nombre" ])
print("Calificaciones del primer estudiante: ", estudiante_uno["Calificaciones"])
