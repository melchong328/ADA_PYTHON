#  Sistema de Reservas de Hotel o Crea una 
# clase Habitacion con atributos como numero, tipo, y precio. 
# Luego, crea una clase Hotel que contenga una lista de habitaciones
#  y métodos para reservar, cancelar y mostrar habitaciones disponibles.

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio

        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} - {self.tipo} - ${self.precio}/noche - {estado}"

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero and habitacion.disponible:
                habitacion.disponible = False
                print(f"Habitación {numero} reservada con éxito.")
                return
        print(f"No se pudo reservar la habitación {numero}.")

    def cancelar_reserva(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero and not habitacion.disponible:
                habitacion.disponible = True
                print(f"Reserva de la habitación {numero} cancelada.")
                return
        print(f"No se pudo cancelar la reserva de la habitación {numero}.")

    def mostrar_habitaciones_disponibles(self):
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                print(habitacion)


hotel = Hotel("Hotel Rosa")

# habitaciones
hotel.agregar_habitacion(Habitacion(101, "Individual", 50))
hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
hotel.agregar_habitacion(Habitacion(103, "Suite", 120))

# Mostrar habitaciones disponibles
hotel.mostrar_habitaciones_disponibles()

# Reservar una habitación
hotel.reservar_habitacion(102)

# Mostrar habitaciones disponibles después de la reserva
hotel.mostrar_habitaciones_disponibles()

# Cancelar una reserva
hotel.cancelar_reserva(102)

# Mostrar habitaciones disponibles después de cancelar
hotel.mostrar_habitaciones_disponibles()