#6-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input('Ingrese aqui un numero entero: '))
if numero%2==0 and numero%3==0:
    print(f'El numero {numero} es multiplo de 2 y de 3')
else:
    print(f'El {numero} no cumple con esa condicion')
    