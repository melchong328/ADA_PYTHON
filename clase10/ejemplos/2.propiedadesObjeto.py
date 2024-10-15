# 2. Propiedades de un Objeto

# Definir La clase persona:
class Persona:
    def init_(self, nombre, edad):
        # inicializar Las pnopiedades del objeto
        self.nombre = nombre # propiedad nombre
        self.edad = edad # propiedad edad

# Crear un objeto de la clase persona
personal = Persona ("Ana", 30)

#Acceder a Las propiedades del objeto
print(personal.nombre)
print (personal.edad)

# La clase persona define un objeto que tilene propiedades como nombre y edad.
# Al instaciar personal con valores especificos, se crean atributos unicos que repr
# el estado de ese objeto.
# Se puede acceder a estas propiedades utiLizando la notacion de punto, Lo que perm
#obtener informacion sobre La instancla creado.