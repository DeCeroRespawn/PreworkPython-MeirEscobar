#Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
print ('escribe una palabra:')
palabra = str(input())
def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]
if es_palindromo(palabra):
  print ('la palabra', palabra, 'es palindromo')
else:
  print ('la palabra', palabra, 'no es palindromo')