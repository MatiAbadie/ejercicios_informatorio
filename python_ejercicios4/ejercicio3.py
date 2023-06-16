#3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
#multiplicar correspondiente a ese número del 1 al 10.

numero = int(input('Ingrese aqui el numero: '))
for i in range(1,10):
    multiplicacion = numero * i
print(multiplicacion)