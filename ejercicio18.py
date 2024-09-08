#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
oracion = input("Ingrese una oración: ")
palabras = oracion.split()
numero_de_palabras = len(palabras)

print("Número de palabras en la oración:", numero_de_palabras)