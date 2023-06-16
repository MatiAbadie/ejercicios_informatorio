#10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
#una vocal o una consonante.

letra = input('Ingrese aqui una letra: ')
if letra in 'aeiouAEIOU':
    print(f'la letra {letra} es una vocal')
else:
    print(f'La letra {letra} es una consonante')

