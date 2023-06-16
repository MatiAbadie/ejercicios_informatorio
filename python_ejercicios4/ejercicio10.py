#10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
#la misma cadena pero con todas las vocales en mayúscula.

texto = input('Ingrese aqui un texto: ')
vocales = ['a','e','i','o','u']

cadena_texto = ''

for caracter in texto:
    if caracter.lower() in vocales:
        cadena_texto += caracter.upper()
    else:
        cadena_texto += caracter
print(f'la cadena de texto con las vocales en mayusculas es {cadena_texto}')

