#Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.

def convertir (milla):
  return (milla*1.60934)/1

millas = float(input('Inserte millas a convertir:'))
print ('la conversion da', convertir(millas))