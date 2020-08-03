nombre = input('Nombre ')
edad = int(input('Edad '))


if edad >= 18:
    print (f'{nombre} Tienes {edad}, Eres MAYOR de edad')
else:
    print (f'{nombre} Tienes {edad}, Eres MENOR de edad')


if nombre.isnumeric():
    print ('es numero')
else:
    print('es letra')

