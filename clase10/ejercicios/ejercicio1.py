#1. Sistema de Gestión de Estudiantes 
#o Crea una clase Estudiante con atributos como nombre, edad, y notas. 
# Implementa métodos para calcular el promedio de notas 
#y determinar si el estudiante ha aprobado o no. Agrega una 
#clase Curso que contenga una lista de estudiantes y un método 
#para mostrar todos los estudiantes aprobados.

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
    
    def calcular_promedio(self):
        # Calcular el promedio sumando todas las notas y dividiendo por la cantidad
        return sum(self.notas) / len(self.notas)
    
    def esta_aprobado(self):
        # Un estudiante aprueba si su promedio es 60 o más
        return self.calcular_promedio() >= 60

# Clase Curso
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def mostrar_aprobados(self):
        print(f"Estudiantes aprobados en {self.nombre}:")
        for estudiante in self.estudiantes:
            if estudiante.esta_aprobado():
                print(f"- {estudiante.nombre}")



estudiante1 = Estudiante("Karla", 20, [70, 80, 90])
estudiante2 = Estudiante("Katia", 22, [50, 60, 70])
estudiante3 = Estudiante("Kamila", 21, [80, 85, 90])

# Crusos donde se agregan los estudiantes
curso_python = Curso("Introducción a Python")
curso_python.agregar_estudiante(estudiante1)
curso_python.agregar_estudiante(estudiante2)
curso_python.agregar_estudiante(estudiante3)

# Mostramos los que aprobaron
curso_python.mostrar_aprobados()