#Escribe un programa que determine si un número ingresado por el usuario es primo o no.

# Función para verificar si un número es primo
def es_primo(numero_usuario):
    if numero_usuario <= 1:
        return False
    for i in range(2, int(numero_usuario**0.5) + 1):
        if numero_usuario % i == 0:
            return False
    return True

# Solicitar al usuario que ingrese un número
numero_usuario = int(input("Ingrese un número: "))

# Verificar si el número es primo y mostrar el resultado
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")