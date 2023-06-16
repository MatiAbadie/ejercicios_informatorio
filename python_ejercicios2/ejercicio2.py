#2-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es positivo, negativo o cero.

numero = float(input('Ingrese aqui un numero: '))
if numero>0:
    print(f'El numero {numero} es positivo')
elif numero<0:
    print(f'el numero {numero} es negativo')
elif numero==0:
    print(f'el numero {numero} es 0')

