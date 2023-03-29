import Initial_Charge as initial
import Incremental_Charge as inc

print('\n1) Realizar carga inicial \n2) Cargar nuevos datos \n3) Salir')
opc = input('\nDigite el numero de la opcion que desea realizar: ')

flag = True

while flag == True:
    if opc == '1':
        print('\nSe realizara la carga inicial de los datos a la base de datos...')
        initial.initial()
        print('\nSe realizo la carga completa de los datos con exito!!')
        flag = False
    elif opc == '2':
        print('\nSe realizara la carga de nuevos datos...')
        inc.incremental()
        print('\nSe cargaron los nuevos datos a la base de datos con exito!!')
        flag = False
    elif opc == '3':
        print('\nSelecciono la opcion de salir \nFeliz dia!!!')
        flag = False
    else:
        opc = input('Opcion incorrecta, digite el numero de una de las opciones: ')