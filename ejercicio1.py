# Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
def conversion_gf():
  return (temperatura_g * 9/5) + 32
temperatura_g = int(input('Escriba la temperatura actual: '))
grados_f = conversion_gf ()
print ('Su temperatura en Grados Fahrenheit es:', grados_f , "°F")