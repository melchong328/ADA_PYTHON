#Ejercicio 3: Eliminar un archivo TXT 
#Escribe un programa que verifique si el archivo archivo_para_eliminar.txt 
#existe. Si existe, elimínalo; si no, muestra un mensaje diciendo que no existe.

import os # importamos modulo

nombre_archivo = 'archivo_para_eliminar.txt'

if os.path.exists(nombre_archivo):

    os.remove(nombre_archivo)
    print(f'Archivo "{nombre_archivo}" eliminado. ')
else:
    #si el archivo no existe, informar al usuario que no se encontro nada
    print(f'El Archivo "{nombre_archivo}" no existe. ')