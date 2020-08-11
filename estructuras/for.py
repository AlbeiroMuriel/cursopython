# imprimir numeros del 1 al 10
# funcion range

for i in range(1,10):
    print ('Numero ' + str(i))

print ('*****************FIN *********')

for i in range(1,20,2):
    print ('Numero ' + str(i))

print ('*****************FIN *********')

for i in range(10,0,-1):
    print(i)

print ('*****************FIN *********')

a =int(input('Ingrese un numero'))
a=a+1
for i in range(1,a):
    print (i)


nroE =int(input('Ingrese un numero Est'))

for i in range(1, nroE + 1):
    nombre= input('Nombre: ')
    n1 = float(input('N1 :'))
    n2 = float(input('N2 :'))
    n3 = float(input('N3 :'))
    nd = (n1 + n2 + n3 )/3
    if nd < 3:
        print (f'Nombre: {nombre} tienes una nota {nd}, debes repetir ')
    else:
        print (f'Nombre: {nombre} tienes una nota {nd}, FELICITACIONES ')


