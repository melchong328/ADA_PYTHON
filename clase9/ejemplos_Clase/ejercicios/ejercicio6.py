#Ejercicio 6: Manejo básico de errores con try/except 
#Crea un programa que solicite al usuario que ingrese un número. Si el 
#usuario ingresa algo que no es un número, muestra un mensaje de error 
#usando try/except.


try:
    numero = int(input("Ingrese un número: "))
    print(f'El número ingresado es: {numero}')
except ValueError:
    print('Error: Debes ingresar un número válido.')