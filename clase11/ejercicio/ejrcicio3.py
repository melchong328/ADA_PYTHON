#Ejercicio 3: Fechas y Tiempos con el Módulo datetime 
#• Objetivo: Trabajar con fechas y tiempos utilizando el módulo 
    #datetime. 
#• Descripción: Calcula la edad de una persona y muestra la fecha actual en diferentes formatos. 
#• Instrucciones: 
#✓ Solicita al usuario su fecha de nacimiento en formato 
    #DD/MM/AAAA. 
#✓ Calcula su edad. 
#✓ Muestra la fecha actual en los siguientes formatos: 
        #Día-Mes-Año. 
        #Mes/Día/Año. 
        #Año/Mes/Día.

from datetime import datetime

# Solicitar fecha de nacimiento
nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
fecha_nac = datetime.strptime(nacimiento, "%d/%m/%Y")

hoy = datetime.now()
edad = hoy.year - fecha_nac.year
if hoy.month < fecha_nac.month or (hoy.month == fecha_nac.month and hoy.day < fecha_nac.day):
    edad -= 1

print(f"\nSu edad es: {edad} años")


print("\nFecha actual:")
print(f"Día-Mes-Año: {hoy.strftime('%d-%m-%Y')}")
print(f"Mes/Día/Año: {hoy.strftime('%m/%d/%Y')}")
print(f"Año/Mes/Día: {hoy.strftime('%Y/%m/%d')}")