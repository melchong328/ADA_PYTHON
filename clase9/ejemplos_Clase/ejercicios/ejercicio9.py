#Ejercicio 9: Usar with/as para manejar archivos 
#Crea un programa que abra un archivo notas.txt, lea su contenido, y lo 
#muestre en la consola. Usa el bloque with para asegurarte de que el 
#archivo se cierra automáticamente.


with open('notas.txt', 'r') as archivo:
    contenido = archivo.read()

print(contenido)