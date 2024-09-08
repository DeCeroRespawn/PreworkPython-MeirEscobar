#Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.

#Variable General y funciones para aplicar el plus de la propina
def totalpropina ():
  return total_restaurante * (15/100)
def totalpagar ():
  return total_restaurante + totalpropina ()

#Insertar los datos
print ('Escriba el total de la cuenta: ')
total_restaurante = int(input())

#Imprimir resultado llamando a la funcion mostrando la propina a aplicar
print ('Cuenta:', total_restaurante)
print ('Propina 15%:', totalpropina ())
print ('total a pagar:', totalpagar ())
