#19-Escribe un programa que solicite al usuario un número decimal y luego
#imprima la parte entera y decimal por separado.

numero = float(input("Ingrese aqui un numero decimal: "))
entero = int(numero)
decimales = round(numero%1,2)
print(f'La parte entera del numero es {entero} y la decimal es {decimales}')