''' 4.	Solicita el nombre de un producto, su precio y cantidad. Calcular:
a.	Subtotal (precio * cantidad)
b.	Descuento del 35% (Subtotal * 35%)
c.	Iva del 19%. (subtotal * 19)
d.	Total a pagar (Subtotal – Descuento + Iva)
e.	Imprimir todos los datos
'''

nombre = input('Nombre Producto: ')
precio = int(input('Precio: '))
cantidad = int(input('Cantidad: '))
descuento = float(input('descuento: '))
iva = 0.19

# realizar calculos 
subtotal = precio * cantidad
VlrDescuento = subtotal * descuento
VlrIva = subtotal * iva
Total = subtotal - VlrDescuento + VlrIva
print('\n')
print('************ DETALLE FACTURA ****************')
print('Valor del producto: ' + str(subtotal))
print('El valor descuento: ' + str(VlrDescuento))
print('Valor Iva: ' + str(VlrIva))
print('El total a Pagar es: ' + str(Total))




