#12-Escribe un programa que pida al usuario una lista de números separados por
#comas y calcule su promedio.

numeros = input('Ingrese aqui una lista de numeros separados por comas: ')
lista_numeros = numeros.split(',')

lista_numeros = [int(n) for n in lista_numeros]
suma = sum(lista_numeros)
promedio = round(suma/len(lista_numeros),2)
print(f'El promedio de la lista de numeros introducida es {promedio}')

    





