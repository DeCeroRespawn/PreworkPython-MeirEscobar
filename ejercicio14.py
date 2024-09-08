#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

#Variable General y funciones para aplicar el plus de la propina
def totaldescuento ():
  return total_producto * (15/100)
def totalpagar ():
  return total_producto - totaldescuento ()

#Insertar los datos
print ('Escriba el total del producto: ')
total_producto = int(input())

#Imprimir resultado llamando a las funciones mostrando la propina a aplicar
print ('Cuenta:', total_producto)
print ('descuento 20%:', totaldescuento ())
print ('total a pagar:', totalpagar ())
