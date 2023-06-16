#9-Escribir un programa que pida al usuario tres números y muestre por pantalla
#el mayor de ellos.

numero1 = float(input('Ingrese aqui el primer numero: '))
numero2 = float(input('Ingrese aqui el segundo numero: '))
numero3 = float(input('Ingrese aqui el tercer numero: '))
if numero1>numero2 and numero1>numero3:
    print(f'El numero {numero1} es el mayor de los tres')
elif numero2>numero1 and numero2>numero3:
    print(f'El numero {numero2} es el mayor de los tres')
elif numero3>numero1 and numero3>numero2:
    print(f'El numero {numero3} el mayor de los tres')