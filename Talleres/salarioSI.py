'''solicitar el nombre y el salario de un empleado.
Si gana menos de 2 Salarios imprimir el nombre, el salario y el aux de transporte
Si gana mas de salarios imprimir solo el nombre, el salario y un mensaje 'No tiene Aux Transporte'.
Tener en cuenta:
Salario minimo. (consultar en Internet)
Auxilio de transporte.(consultar en Internet)
'''

print ('**************SALARIO Y AUX TRANSPORTE **********\n')

name = (input('Nombre: '))
salary= int(input('Salario: ') )

smlv = 877803
auxT = 102854

if salary <= smlv * 2:
    print(f'Nombre: {name} ')
    print(f'Salario: {salary}')
    print(f'Aux Transp: {auxT}')
    print('El total a pagar es: ', salary + auxT)
else:
    print(f'Nombre: {name} ')
    print(f'Salario: {salary} y no tienes derecho a Auxt Trans, gana mucho')




    