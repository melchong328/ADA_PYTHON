#Buscar y Imprimir la Edad de un Estudiante en un Diccionario Anidado

#1. Crea un diccionario que represente una clase con los siguientes datos: 
#o nombre_clase 
#o estudiantes, que es una lista de diccionarios con información de cada estudiante (nombre y edad). 
#2. Escribe una función que busque la edad de un estudiante dado su nombre usando el índice de la lista en lugar de bucles (suponiendo que conoces el índice). 
#3. Imprime la edad del estudiante buscado.

clase = {
    'nombre_clase' : 'Artes',
    'estudiantes' : [{'nombre' : 'Ana','edad' : 15},
                    {'nombre' : 'Julian','edad' : 17},
                    {'nombre' : 'Caro','edad' : 13},
                    {'nombre' : 'Martha','edad' : 14},
                    ]
}

def buscar_edad_estudiante(Clase, nombre_estudiante):
    return Clase['estudiantes'][nombre_estudiante]['edad']

indice_estudiante = int(input('Ingrese el indice del estudiante: '))

edad = buscar_edad_estudiante(clase, indice_estudiante)
print(f'La edad del estudiante {indice_estudiante} es: {edad}')