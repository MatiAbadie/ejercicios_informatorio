#8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
#el número de palabras que contiene

texto = input('Ingrese aqui un texto: ')

texto_lista = texto.split()
cantidad_palabras = len(texto_lista)

print(cantidad_palabras)

