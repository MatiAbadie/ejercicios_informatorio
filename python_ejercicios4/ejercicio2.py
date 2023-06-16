#2-Escribe un programa que pida al usuario un número y calcule la suma de todos
#los números naturales del 1 hasta ese número.

numero = int(input('Ingrese aqui un numero: '))
suma = 0
for i in range(1, numero+1):
  suma = suma + i
print(suma)