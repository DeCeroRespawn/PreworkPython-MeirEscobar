#Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
# Inicializar contadores
impares = 0
pares = 0
numeros = []  # Lista para almacenar los números ingresados

while True:
    entrada = input('Ingrese un número (o escriba "salir" para terminar): ')
    
    # Opción para salir del bucle
    if entrada.lower() == 'salir':
        break
    
    # Intentar convertir la entrada a un entero
    try:
        numero = int(entrada)
        numeros.append(numero)
        
        # Contar pares e impares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    except ValueError:
        print('Error: Asegúrese de ingresar un número entero válido.')


print(f'Su lista de números es: {numeros}')
print(f'Cantidad de números pares: {pares}')
print(f'Cantidad de números impares: {impares}')