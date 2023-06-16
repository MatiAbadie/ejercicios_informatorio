#9-Escribe un programa que pida al usuario un número y luego imprima la
#secuencia de Fibonacci correspondiente a ese número.

numero = int(input('Ingrese aqui un numero: '))
fib_secuencia = [0,1]

while len(fib_secuencia) < numero:
    siguiente_numero = fib_secuencia[-1] + fib_secuencia[-2]
    fib_secuencia.append(siguiente_numero)
print(fib_secuencia)
     




