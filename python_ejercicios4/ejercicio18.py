#18-Escribe un programa que pida al usuario un número y luego imprima un
#triángulo de números como el siguiente:
#1
#2 3
#4 5 6
#7 8 9 10

numero = int(input('Ingrese aqui un numero: '))
contador = 1

for i in range(1,numero + 1):
    for j in range(1, i + 1):
        print(contador, end=' ')
        contador += 1
    print() 
   
