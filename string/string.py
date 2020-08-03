micadena = 'Bienvenidos al Curso'

#print(dir(micadena))

print(micadena.upper())
print(micadena.lower())
print(micadena.capitalize())
print(micadena.swapcase())

#count, cuenta el numero de veces que aparece una letra
print(micadena.count('e'))

#startswith, devuelve False o True si la palabra comienza con dicho texto
print(micadena.startswith('Bien'))
#endswith, termina en 
print(micadena.endswith('so'))

#split separa el texto por palabras
print(micadena.split())

#split separa el texto por palabras o por una letra especifica
print(micadena.split('o'))


#find, devuelve nro de la primer posicion de un letra, comienza el cero
print(micadena.find('o'))

#len, tamaño de la cadena
print(len(micadena))

#index, devuelve la posición
print(micadena.index('e'))

print(micadena.isnumeric())
print(micadena.isalpha())


print(micadena[-2])




