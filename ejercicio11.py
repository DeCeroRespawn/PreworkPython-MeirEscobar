#Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
from datetime import datetime
now = datetime.now()
def calculo_edad (año_usuario):
  return now.year - año_usuario
print (now.year)
año_usuario = int(input('inserte su edad:'))
print (calculo_edad (año_usuario))

