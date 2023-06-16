#16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
#e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = 

peso = float(input('Ingrese aqui su peso: '))
altura = float(input('Ingrese aqui su altura: '))
imc = peso / (altura ** 2)
print(f'Su indice de masa corporal es de {imc}')