# Ejercicio 5: Escribir en un archivo CSV 
# Crea un programa que guarde los siguientes datos en un archivo CSV

import csv
with open('alumnos.csv', 'w', newline ='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre', 'Edad'])
    escritor.writerow(['Karla', 21])
    escritor.writerow(['Katia', 23])
