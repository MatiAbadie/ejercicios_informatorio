#5-Escribe un programa que imprima la suma de todos los números pares del 1 al
#100.

suma = 0

for i in range(1, 100):
  if i % 2 == 0:
   suma += i
   print(suma)
