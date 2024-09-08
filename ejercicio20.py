#Crea un programa que sume todos los números en una lista ingresada por el usuario.

# Pedir los números separados por comas o espacios
num = input('Coloca los números separados por comas, espacios o ambos: ')

# Reemplazar las comas por espacios, luego dividir por los espacios
num_list = [int(x) for x in num.replace(',', ' ').split()]

# Sumar los números
suma = sum(num_list)

# Imprimir el resultado
print(suma)
