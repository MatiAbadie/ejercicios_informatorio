#15-Escribe un programa que pida al usuario una cadena de texto y determine
#cuántas veces aparece cada letra en la cadena.

texto = input('Ingrese aqui un texto: ')
frecuencia_letras = {}

for letra in texto:
    if letra in frecuencia_letras:
        frecuencia_letras[letra] += 1
    else:
        frecuencia_letras[letra] = 1
print('la frecuencia de letras en la cadena es de: ')

for letra, frecuencia in frecuencia_letras.items():
    print(f"La letra '{letra}' aparece {frecuencia} veces")

