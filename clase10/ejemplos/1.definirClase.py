# definir una clase en python

# definimos una clase llamada coche
class Coche:
    # emtodo __init__ es el constructor que se llama al crear un nuevo objeto
    def __init__(self, marca, modelo):
        # self es una referencia al objeto que estamos creando
        # inicializamos los atributos de la instancia
        self.marca = marca # Atributo de instancia: guarda la marca del coche
        self-modelo - modelo # Atributo de instancia: guarda el modelo del coche
        
# La clase coche es una plantilla para crear objetos de tipo auto.
# Contiene un metodo constructor -init_ que inicializa los atributos especificos -
# como por ejemplo: marca, modelo usando la referencia self para distinguir entre L
# del objeto y los parametros pasados al constructor.l