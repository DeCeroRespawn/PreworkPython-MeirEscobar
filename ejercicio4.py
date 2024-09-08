#Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario
vocales = 'aeiouAEIOU'
total_vocales = 0
print ('Escriba una palabra:')
palabra = input()
for contar_vocales in palabra : 
  if contar_vocales in vocales:
    total_vocales += 1
print (total_vocales)
