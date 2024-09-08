#Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
semana = { '1':'Lunes',
        '2':'Martes',
        '3':'Miercoles',
        '4':'Jueves',
        '5':'Viernes',
        '6':'Sabado',
        '7':'Domingo'}
numero = (input('Escriba un numero del 1 al 7:'))
if numero in semana:
    print(f"{numero}: {semana[numero]}")