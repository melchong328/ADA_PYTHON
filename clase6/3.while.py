# Programa para adivinar un numero secreto
# Definimos el numero secreto
numero_secreto = 7

#Inicializar la variable para almacenar el numero del ususario
numero_advinado = None

# Mensaje inicial
print('Advinar el numero secreto (entre 1 y 10): ')

# Bucle while que continua hasta que el ususario advine el numero secereto
while numero_advinado != numero_secreto:
    #Solicitar al ususario que ingrese un numero
    numero_advinado = int(input('Introduce tu numero: '))

    #comporbar si el numero advinado es correcto
    if numero_advinado < numero_secreto:
        print('Demasiado bajo. Intenta de nuevo. ')
    elif numero_advinado > numero_secreto:
        print('Demasiado alto. Intenta de nuevo. ')
    else: 
        print('Felicidasdes has advinado el numero secreto!' )

#Mensaje de finalizacion del juego
print('Gracias por jugar! ')

