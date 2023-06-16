caracter = input('Inserte aqui el caracter: ')
if caracter.isupper():
    print('el caracter es mayuscula')
elif caracter.islower():
    print('el caracter es minuscula')
elif caracter.isdigit():
    print('el caracter es un numero')
else:
    print('el caracter es un caracter especial')