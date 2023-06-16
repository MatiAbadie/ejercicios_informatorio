#3-Escribir un programa que pida al usuario dos números y muestre por pantalla
#cuál de ellos es mayor.

primer_numero = float(input('Ingrese aqui el primer numero: '))
segundo_numero = float(input('Ingrese aqui el segundo numero: '))
if primer_numero>segundo_numero:
    print(f'El mayor numero es {primer_numero}')
else:
    print(f'El mayor numero es {segundo_numero}')