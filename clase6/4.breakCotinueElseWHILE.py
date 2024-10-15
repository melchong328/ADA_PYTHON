# Programa que pide numero hasta que se ingrese un numero negativo
# Numero positivos ingresados
suma = 0 

# Inicializamos un ciclo infinito usando while true
while True: 
#Solicitamos al ususario que introdusca un numero
#La entrada se convierte en numero entero
    entrada = int(input('Introduce un numero (negativo para terminar): '))

    # Verificamos si el numero ingresado es negativo
    if entrada < 0:
        # Si el numero es negativo, salimos del ciclo usando
        break
    
    #Sumamos el numero positivo ingresando a la variable suma
    suma += entrada 

    # Verificar si el numero ingresado es par
    if entrada % 2 == 0:
        # Si el numero es par, usamos continue para saltar la impresion
        # y pasar a la siguiente iteracion del ciclo
        continue
    # Si el numero ingresado no es par (es impar), se ejecuta esta linea: 
    print(f'Numero impar ingresado: {entrada}')

else:
    print(f'El ciclo ha terminado porque se ingreso un numero negativo.')

#Mensaje final
print(f'La suma de los numeros ingresados es: {suma}. ')

