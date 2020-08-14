def mensaje():
    print('hola mundo')

def retornarNombre(name='No ingreso valor'):
    print (f'Hola {name} como estas....')


def suma(a, b):
    return  a + b

     
if __name__ == "__main__":
    mensaje()

    # funciones con parametros
    retornarNombre('albeiro')
    retornarNombre('Liliana')
    retornarNombre()

    print(suma(50,100))

    






