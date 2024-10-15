#Ejercicio 2: Escribir en un archivo TXT 
#Crea un programa que escriba un texto en un archivo nuevo_archivo.txt. Si 
#el archivo ya existe, debe sobrescribir su contenido.


with open('nuevo_archivo.txt', 'w') as file:
    file.write('Este archivo fue sobrescrito por el modo \'w\'.\n')
    file.write('Todo el contenido previo fue eliminado.')
print("Archivo 'nuevo_archivo.txt' creado con exito.")

with open('nuevo_archivo.txt', 'x') as file:
    file.write('Este archivo fue creado con exito usando \'x\'.\n')
print("Archivo 'nuevo_archivo.txt' creado con exito.")

