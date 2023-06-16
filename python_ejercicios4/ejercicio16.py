#16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
#la misma cadena pero con cada palabra al revés.

texto = input('ingrese aqui el texto: ')
texto_lista = texto.split()
palabras_invertidas = [palabra[::-1] for palabra in texto_lista]
texto_palabras_invertidas = (' ').join(palabras_invertidas)
print(texto_palabras_invertidas)