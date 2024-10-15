# Diccionario dentro de una Lista 

#1. Crea una lista de diccionarios donde cada diccionario representa un producto en una tienda, con claves: 
#o Nombre 
#o Precio 
#o Cantidad en stock 
#2. Imprime el nombre y el precio del segundo producto en la lista. 

Productos_tienda = [{
    'Nombre': 'leche',
    'Precio' : '30',
    'Cantidad en stock' : 87
},
{
    'Nombre': 'azucar',
    'Precio' : '20',
    'Cantidad en stock' : 160
},
{
    'Nombre': 'aguacate',
    'Precio' : '60',
    'Cantidad en stock' : 100
}
]

segundo_producto = Productos_tienda[1]
nombre = segundo_producto.get("Nombre")
precio = segundo_producto.get("Precio")

print(f'El nombre del producto es {nombre} y su precio es de {precio} pesos mexicanos.')