'''
Solicitar el nombre de un estudiante, el estrato y el valor de la matrícula.
Se le concederé un descuento dependiendo de las siguientes condiciones.

* Estrato = 1 el descuento será del 60%
* Estrato = 2 el descuento será del 50%
* Estrato = 3 el descuento será del 40%
* Estrato = 4 el descuento será del 30%
* Estrato = 5 el descuento será del 1%
* Estrato = 6 Se incrementará el valor en un 10%

Imprimir el Nombre, el valor de la matrícula, el descuento y el total a pagar.
Nota en el estrato 6. el Nombre, el valor de la matrícula, el incremento y el total a pagar.

'''

print('**************** DESCUENTO MATRICULA *******************')

name = input('Nombre: ')
est = int(input('Estrato: '))
matric = int(input('Vlr Matrícula: '))
desc = 0

if est >= 1 and est <= 6:
    if est == 1:
        desc= matric * 60/100
    elif est == 2:
        desc= matric * 50/100
    elif est == 3:
        desc= matric * 40/100
    elif est == 4:
        desc= matric * 30/100
    elif est == 5:
        desc= matric * 1/100
    else:
        aum = matric * 10/100
        print('****** Valor a Pagar *********** \n')

        print(f'Nombre          | {name}')
        print(f'Estrato         | {est} ')
        print(f'Matrícula       | {matric}')
        print(f'Descuento       | {desc}')
        print(f'Total a pagar   |',matric + aum)
        exit()
else:
    print(f'Verifique el numero del estrato, este numero {est}, no es valido')
    exit()

print('****** Valor a Pagar *********** \n')
print('────────────────┬───────────────────────')
print(f'Nombre          │ {name}')
print(f'Estrato         │ {est} ')
print(f'Matrícula       | {matric}')
print(f'Descuento       | {desc}')
print(f'Total a pagar   |',matric - desc)
print('────────────────┴──────────────────────')

