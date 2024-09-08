#Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
def suma100():
  cien = 0
  suma = 0
  while cien <= 100:
    cien += 1
    if cien % 2 == 0:
      suma += cien
  return suma
print (suma100())