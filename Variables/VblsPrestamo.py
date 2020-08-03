''' 2.	Solicitar el nombre del cliente, el valor de un préstamo, 
el número de cuotas, el valor del interés (escribir el interés con formato decimal ejemplo 5% equivale al 0.05).
Calcular el valor del interés mensual. Imprimir el nombre, el valor de préstamo, 
el interés, el valor de interés mensual, el número de cuotas, y el valor total a pagar.'''

nombre = input('Nombre: ')
prestamo = int(input('Vlr Prestamo: '))
interes = float(input('Vlr interes en % '))
cuotas = int(input('Nro de cuotas: '))
intmes = prestamo * interes
ttalpagar = prestamo + intmes * cuotas

print('********** RESULTADOS *********** \n\n')
print('Nombre: ' + nombre)
print('Vlr Prestamo: ' + str(prestamo))
print('Vlr interes: '+ str(interes))
print('Nro cuotas: ' + str(cuotas))
print('Vlr interes mes' + str(intmes))
print('Total a pagar ' + str(ttalpagar))

