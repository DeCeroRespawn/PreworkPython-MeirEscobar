#Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
print ('______________________')
print ('operaciones disponibles:')
print ('----------------------')
print ('1-suma')
print ('2-resta')
print ('3-multiplicacion')
print ('4-division')
print ()
print('escoja una opcion de la lista de "operaciones disponibles"')
operacion = int(input())
print ('primer numero a operar:')
numero1 = float(input())
print ('segundo numero a operar:')
numero2 = float(input())

if operacion == 1:
  print (f'la suma es', numero1+numero2)
elif operacion == 2:
  print (f'la resta es', numero1-numero2)
elif operacion == 3:
  print (f'la multiplicacion es', numero1*numero2)
elif operacion == 4:
  print (f'la division es', numero1/numero2)