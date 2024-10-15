# Crear y Acceder a un Diccionario Básico 

# 1. Crea un diccionario que contenga la siguiente información sobre un libro: 
# o Título 
# o Autor 
# o Año de publicación 
# o Género 
# 2. Accede e imprime cada uno de estos valores usando las claves correspondientes.

Libro = {
    'Titulo' : 'Daisy Jones & the Six',
    'Autor' : 'Taylor Jenkins Reid',
    'Año de publicación' : 2019,
    'Género' : 'Novela'
}

Titulo = Libro['Titulo']
Autor = Libro['Autor']
Año_de_publicación = Libro['Año de publicación']
Género = Libro['Género']

print('Titulo: ', Titulo)
print('Autor: ', Autor)
print('Año de publicación: ', Año_de_publicación)
print('Género: ', Género)

