fecha_nacimiento = input('Inserte aqui su fecha de nacimiento en formato dd/mm/aaaa') 
dia, mes, anio = fecha_nacimiento.split('/')
edad = 2023-int(anio)
print(f'Tu edad es de {edad}')

