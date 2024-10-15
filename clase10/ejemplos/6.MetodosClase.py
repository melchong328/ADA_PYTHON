# 6. Metodos de clase

# Definimos una clase
class Conejo:
    cantidad_de_conejos = 0 # Atributo de clase

    def init__(self, color, nombre):
        self.color = color # Atributo de instancia
        self.nombre = nombre # Atributo de instancia
        Conejo. cantidad_de_conejos += 1 # Aumenta La cantidad total de conejos

# Metodo de clase para obtener el total de conejos
@classmethod
def total_conejos(cLs):
    return f"Total de conejos: {cls.cantidad_de_conejos}"

# Crear instancias de la clase conejo
conejo1 = Conejo("Blanco", "Tambor")
conejo2 = Conejo("Gris", "Pochoclo")

# Llamar al metodo de clase
print(Conejo.total_conejos())

# La clase conejo incluye un metodo de clase total_conejos, que se utiliza para acc
# a un atributo de clase (cantidad_de_conejos). Este metodo permite realizar operac
# que afectan a la clase en su totalidad, en Lugar de a instancias individuales,
# Lo que facilita el seguimiento de cuantos objetos de esa clase han sido creados.