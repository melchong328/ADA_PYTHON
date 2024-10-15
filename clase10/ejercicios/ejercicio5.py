#Clases de Vehículos o Crea una clase base Vehiculo que tenga atributos marca y modelo. 
# #Luego, crea subclases Coche y Motocicleta que hereden de Vehiculo. Implementa el método mostrar_info() en cada subclase que utilice super() para mostrar la información 
# básica y luego la específica de cada vehículo.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Subclase Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica}, Puertas: {self.puertas}"

# Subclase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica}, Tipo: {self.tipo}"

coche1 = Coche("Toyota", "Corolla", 4)
moto1 = Motocicleta("Honda", "CBR", "Deportiva")

print("Información del coche:")
print(coche1.mostrar_info())

print("\nInformación de la motocicleta:")
print(moto1.mostrar_info())