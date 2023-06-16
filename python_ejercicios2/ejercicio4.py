#4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
#pantalla si está aprobado (5 o más) o no.

nota = int(input('Ingrese aqui una nota: '))
if nota>=6:
    print('Aprobado')
else:
    print('Desaprobado')