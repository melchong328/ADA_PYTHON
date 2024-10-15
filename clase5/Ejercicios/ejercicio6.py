#Anidación Compleja de Diccionarios y Listas 

#1. Crea un diccionario que contenga información sobre una escuela. La escuela tiene: 
# o Nombre 
# o Año de fundación 
# o Lista de clases, donde cada clase es un diccionario con: 
# ▪ Nombre de la clase 
# ▪ Lista de estudiantes, donde cada estudiante es un diccionario con: 
# ▪ Nombre 
# ▪ Edad 
# 2. Imprime el nombre del primer estudiante de la primera clase.

Escuela = {
    'Nombre' : '18 de marzo',
    'Año de fundación' : 1990,
    'Clases' : [
        {
        "Nombre de la clase" : 'Artes',
        'Estudiantes' : [
            {'Nombre' : 'Luis','Edad' : 10},
            {'Nombre' : 'Anna','Edad' : 9},
            {'Nombre' : 'Sofi','Edad' : 10}]},{
        'Nombre de la clase' : 'Ciencias',
        'Estudiantes' : [
            {'Nombre' : 'Azul','Edad' : 11},
            {'Nombre' : 'Miguel','Edad' : 9},
            {'Nombre' : 'Mario','Edad' : 9}
        ]
        } 
    ]}

Primer_estudiante = Escuela["Clases"][0]['Estudiantes'][0]['Nombre']
print(Primer_estudiante)