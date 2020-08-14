dic1 = {'nombre' : 'albeiro', 'cedula':123456,  'cargo': 'docente', 'salario': 1500}

#agregar una nueva clave
dic1['horario']='12 pm'
print(dic1, '\n')

print('Cedula ', dic1['cedula'])


for key in dic1:
  print (key, ":", dic1[key])

#keys()
# Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.


print ('***** devuelve las llaves ********** \n')
keys = dic1.keys()
print(keys)
print ('***** devuelve las llaves ********** \n')



#values()
#Retorna una lista de elementos, que serán los valores de nuestro diccionario.
print ('***** devuelve las valores  ********** \n')
vals = dic1.values()
print(vals)
print ('***** valores ********** \n')


#pop()
#Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra,
# devuelve error.

eliminar = dic1.pop('cedula')
print(dic1, '\n')
print(eliminar)



#cambiar el vlalor de un dato
# si el dato existe lo modifica
# sino lo crea
dic1['nombre']= 'muriel'
print(dic1)

#get busca un dato, sino lo encuentra se le puede asignar un valor
#se busca por la clave o llave
print(dic1.get('nombre','Dato no encontrador'))

print('nombre ', dic1['nombre'])


#eliminar un diccionario
dic1.clear()
print(dic1)