# Clases de Formas Geométricas 
# o Define una clase base Forma con un método area().
# Luego, crea subclases Rectangulo, Circulo, y Triangulo que implementen el método area() de manera específica. 
# Usa polimorfismo para crear una lista de formas y calcular el área de cada una.

import math

# Clase base Forma
class Forma:
    def area(self):
        pass  # Método para las subclases

# Subclase Rectangulo
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

# Subclase Circulo
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2

# Subclase Triangulo
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return 0.5 * self.base * self.altura

# Función para calcular y mostrar el área de las formas
def mostrar_area(forma):
    print(f"El área de la {forma.__class__.__name__} es: {forma.area():.2f}")

# Crear una lista de formas
formas = [
    Rectangulo(5, 4),
    Circulo(3),
    Triangulo(6, 8)
]

# Calcular y mostrar el área de cada forma
for forma in formas:
    mostrar_area(forma)