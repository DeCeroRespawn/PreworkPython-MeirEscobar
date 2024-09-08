#Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.

minutos = int(input("Ingrese el número de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")