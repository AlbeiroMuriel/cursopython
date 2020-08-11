micadena = 'Bienvenidos al Curso. Este mensaje esta en mayúscula\n'
print(micadena.upper())


micadena = 'Bienvenidos al Curso. Este mensaje esta en MINUSCULA\n'
print(micadena.lower())

#split separa el texto por palabras
print(micadena.split())


#split separa el texto por palabras o por una letra especifica
print(micadena.split('o'))


#len, tamaño de la cadena
print(len(micadena))



'''
#micadena = 'bienvenidos al curso CAPITALIZE.\n'
#print(micadena.capitalize())

micadena = 'bienvenidos al curso. con SWAPcase\n'
print(micadena.swapcase())


#count, cuenta el numero de veces que aparece una letra
print(micadena.count('e'))

#startswith, devuelve False o True si la palabra comienza con dicho texto
print(micadena.startswith('Bien'))
#endswith, termina en 
print(micadena.endswith('so'))

#find, devuelve nro de la primer posicion de un letra, comienza el cero
print(micadena.find('o'))

#index, devuelve la posición
print(micadena.index('e'))

print(micadena[-2])

'''