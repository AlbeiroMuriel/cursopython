def ejercicio1():
    # Numero de empleados
    nroEmp = int(input('Numero de empleados :'))
    tsalario = 0
    for i in range(0, nroEmp):
        Nombre = input('Nombre: ')
        salario = int(input('Salario'))
        print(f'{Nombre} tu salario es de {salario} el dia vale {salario/30} y la hora {salario/240}')        
        tsalario = tsalario + salario      
    
    print(f'El Total de salarios de {tsalario} y el numero de empleados es de {nroEmp}')

def ejercicio2():
    print('*************** EJERCICIO 2 **************************')
    for i in range(10):
        print(i)



def ejercicio3():
    print('*************** EJERCICIO 3 **************************')
    for i in range(5,10):
        print(i)
    
    print ('fin ejercicio 2')

def ejercicio4():
    pass


if __name__ == "__main__":
    print ('********** menu ************' )
    print ('1 - Empleados')
    print ('2 - Numeros')
    print ('3 - intervaos')
    print ('4 - Salir')
    op = int(input('Seleccione un Nro '))
    if op == 1:
        ejercicio1()
    elif op == 2:
        ejercicio2()
    elif op == 3:
        ejercicio3()    
    else: exit


    


