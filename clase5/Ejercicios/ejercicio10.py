# Buscar y Actualizar la Información en un Diccionario Anidado 

#1. Crea un diccionario que represente una base de datos de empleados de una empresa. El diccionario debe tener: 
#o nombre_empresa 
#o empleados, que es una lista de diccionarios, donde cada diccionario representa un empleado con: 
#▪ id_empleado 
#▪ nombre 
#▪ departamento 
#▪ salario 
#2. Escribe una función que busque y actualice el salario de un empleado dado su id_empleado. La función debe: 
#o Buscar el empleado por su id_empleado. 
#o Actualizar el salario del empleado a un nuevo valor proporcionado. 
#o Imprimir la información del empleado después de la actualización.

datos_empleados = {
    'nombre_empresa' : 'Luna',
    'empleados' : [
        {'id_empleado' : 2222, 'nombre' : 'Ana', 'departamento' : 'recursos humanos', 'salaio' : 6000},
        {'id_empleado' : 2323, 'nombre' : 'Miguel', 'departamento' : 'cajero', 'salaio' : 3000},
        {'id_empleado' : 2424, 'nombre' : 'Brandy', 'departamento' : 'almacen', 'salaio' : 5000}
    ]
}

