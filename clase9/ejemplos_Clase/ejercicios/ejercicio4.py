#Ejercicio 4: Leer un archivo CSV 
#Crea un programa que lea los datos de un archivo CSV datos.csv y muestre cada fila en la consola. 

import csv

with open('datos.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)