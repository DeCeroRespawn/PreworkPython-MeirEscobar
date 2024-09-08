# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
def imc ():
  altura_dos = altura*altura
  return kg/altura_dos
print ('Inserte aqui su peso:')
kg = float(input())
print ('Inserte aqui su altura:')
altura = float(input())
resultado = imc ()
print ('tu imc es', ('{:.2f}'.format(resultado)))