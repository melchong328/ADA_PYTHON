# Ejercicio 1: Leer un archivo TXT 
#Crea un programa en Python que lea el contenido de un archivo 
#mi_archivo.txt y muestre cada línea en la consola. El archivo tiene varias

nombre_archivo = 'mi_archivo.txt'

with open (nombre_archivo, 'r') as archivo:
    print("Leyendo el archivo linea por linea con readline(): ")
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()
    print("-" * 40)