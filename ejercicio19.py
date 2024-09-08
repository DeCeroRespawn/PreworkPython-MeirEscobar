#Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
año = int(input('Introduce un año: '))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')