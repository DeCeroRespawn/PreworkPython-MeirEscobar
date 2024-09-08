#Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
def convertir (dolares):
  return (dolares*0.85)/1

dolares = float(input('Inserte dolares a convertir:'))
print ('la conversion da', convertir(dolares))