#Modificar un Valor en un Diccionario Anidado 

#1. Crea un diccionario que contenga información sobre una tienda de libros, con las siguientes claves: 
#o nombre_tienda 
#o libros, que es una lista de diccionarios, donde cada diccionario representa un libro con claves titulo y precio. 
#2. Cambia el precio del segundo libro en la lista a un nuevo valor (por ejemplo, 15.99). 
#3. Imprime el título y el precio del segundo libro después de la modificación.

Tienda_libros = {
    'nombre_tienda' : 'Libreria oruga',
    'libros' : [{'titulo' : 'Los juegos del hambre','precio' : 140}, 
                {'titulo' : 'Orgullo y prejuicio','precio' : 250}, 
                {'titulo' : 'Sinsajo','precio' : 178}, 
                {'titulo' : 'En llamas','precio' : 476}, 
                {'titulo' : 'Como agua para chocolate','precio' : 358}
                ]
}

Tienda_libros['libros'][1]['precio'] = 15.99

segundo_libro = Tienda_libros['libros'][1]

print(segundo_libro)