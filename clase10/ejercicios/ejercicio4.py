# Sistema de Inventario o Define una clase Producto con atributos como nombre, precio, y cantidad. 
# Agrega métodos para aumentar o disminuir la cantidad de productos. 
# Luego, crea una clase Inventario que contenga una lista de productos y métodos para agregar y mostrar productos.

# Definir la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"{self.nombre} - Precio: ${self.precio}, Cantidad: {self.cantidad}")

# Definir la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Se agregó {producto.nombre} al inventario")

    def mostrar_productos(self):
        print("Productos en el inventario:")
        for producto in self.productos:
            producto.mostrar_info()

manzanas = Producto("Manzanas", 0.5, 100)
leche = Producto("Leche", 2.5, 50)
pan = Producto("Pan", 1.0, 30)

#  crear inventario
mi_inventario = Inventario()

# Agregar productos al inventario
mi_inventario.agregar_producto(manzanas)
mi_inventario.agregar_producto(leche)
mi_inventario.agregar_producto(pan)

# Mostrar todos los productos en el inventario
mi_inventario.mostrar_productos()