'''Realizar un programa que calcule el salario de N empleados.
Se tienen los siguientes datos
Nombre, salario, #extras y #horasdominicales
Se debe calcular:
El valor día (salario /30)
El valor hora (salario /240)
vlrHoraExtra: 1.35 del valor de la hora (35%)
vlrHoradominical: 1.75 del valor de la hora. (75%)
vlrExtrasTotal = ¿?
vlrdominicalTotal =¿?

Imprimir
Nombre, Salario, Valor del día, Valor de la hora, Horas Extras,Valor de la extra
El Total a pagar por extras,Horas dominicales,Valor de la hora dominical
El total a pagar por horas dominicales,
Y El total a pagar. (Salario + vlrExtrasTotal +  vlrdominicalTotal)

****************************************************
*Si el Tota la pagar es menor de 1 millon. Mensaje. {Nombre} solicita aumento.

*Si el Total a pagar es menor de 2 millon. 
    Realizar una retención del 1%
    Mensaje. {Nombre}, su salario es de {Total a pagar} y la retención es de {retencion}

* Si el Total a pagar es menor o igual de 3 millon. 
    Realizar una retención del 3%
    Mensaje. {Nombre}, su salario es de {Total a pagar} y la retención es de {retencion}

* Si el Total a pagar es mayor de 3 millon. 
    Realizar una retención del 4%
    Mensaje. {Nombre}, su salario es de {Total a pagar} y la retención es de {retencion}
'''

print('****************CALCULAR SALARIO ******************\n')
name = input('Nombre: ')
salary = int(input('Salario: '))
extras = int(input('Nro Extras: '))
extraSunday = int(input('Extras Domin:'))
salDay = salary/30
saltime = salary/240
vlrExtras = saltime * extras * 1.35
vlrSunday = saltime * extraSunday * 1.75
ret = 0
totalPag = salary + vlrExtras + vlrSunday

if totalPag < 1000000:
    mensaje = 'Solicita Aumento'
elif totalPag < 2000000:
    ret = totalPag * 1/100
elif totalPag < 3000000:
    ret = totalPag * 3/100
elif totalPag >= 3000000:
    ret = totalPag * 4/100

print('───────────────┬───────────────────────')
print(f'Nombre         │ {name}')
print(f'Salario        │ {salary}')
print(f'Vlr Dia        | {salDay}')
print(f'Vlr Hora       | {saltime}')
print(f'Horas Extras   | {extras}')
print(f'Vlr Extras     | {vlrExtras}')
print(f'H Ext Domin    | {extraSunday}')
print(f'Vlr Ext Domin  | {vlrSunday}')
print(f'Total a pagar  | {totalPag}')
print('───────────────┴──────────────────────\n')


print('────────────────────────────────────────')
print(f'{name}, su salario es de {totalPag} \n y la retención es de {ret} \n por lo tanto su pago es de {totalPag - ret}')
print('────────────────────────────────────────\n')





