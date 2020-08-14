from os import system
system("cls")


# Aceptar solo cadenas de texto
i=1
while i <= 10 :
    print(i)
    i+=1


nombre = 'Albeiro'
while nombre.isalpha():
    print(nombre)
    nombre = (input('nombre '))

r = True
while r:
    r = input('digite un nro ')
    if not r.isnumeric():
        r = False
else:
    print ('digito texto')


r = input('Desea continuar S/N ')
while r.lower() == 's':
    r = input('Desea continuar S/N ')


