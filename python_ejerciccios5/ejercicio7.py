#7-Crea una función llamada imprimir_pares que tome un número entero como
#parámetro y imprima todos los números pares desde 1 hasta ese número.

def imprimir_pares(numero):
    for i in range(1, numero+1):
        if i%2==0:
            print(i)

imprimir_pares(8)


   