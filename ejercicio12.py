# Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.

def calculo_area (long, anc):
  return long * anc

long = int(input('indique la longitud:'))
anc = int(input('indique anchura:'))
area = calculo_area (long, anc)

calculo_area (long, anc)
print ('el area del rectangulo es', area)