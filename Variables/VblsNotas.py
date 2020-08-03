print ('with AREPL')

''' 3.	Solicitar el nombre del estudiante, y tres notas. 
a.	La nota 1 tiene un valor del 25%, 
b.	La nota 2 tiene un valor del 35% 
c.	La nota 3 un valor de 4%
d.	Imprimir el nombre, la nota el % y el valor del porcentaje, y la nota final. Ejemplo
Nombre	Albeiro
N1 – 4.5    25%  -- 1.12
N2 – 3.5    35%  -- 1.22	
N3 – 2.0    40%  -- 0.80	
Definitiva – 3.15
'''

nombre = input('Nombre ')
n1 = float(input('Nota 1 --> '))
n2 = float(input('Nota 2 --> '))
n3 = float(input('Nota 3 --> '))

#realizar calculos

definitiva = n1 * 0.25 + n2 * 0.35 + n3 * 0.4

print('**************** RESULTADOS ****************** \n\n')
print(nombre)
print(f'Nota 1 es de {str(n1)} vale el 25%  --> ' + str(float(n1) *0.25 ))
print(f'Nota 2 es de {str(n2)} vale el 25%  --> ' + str(float(n2) *0.35 ))
print(f'Nota 3 es de {str(n3)} vale el 25%  --> ' + str(float(n3) *0.4 ))
print(f'El resultado de su Nota Definitiva es de {str(definitiva)} \n')

print('**************** FIN NOTA DEFITIVA ****************** \n\n')