#14-Escribe un programa que pida al usuario un número y luego imprima un
#triángulo de números como el siguiente:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

numero = int(input('Ingrese aqui un numero: '))
numero_caracter = str(numero)
triangulo = ''
i = 1

while i <= numero:     
     triangulo += numero_caracter*i + '\n'
     i += 1
print(triangulo)

