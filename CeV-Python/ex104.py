def LeiaInt(texto):
	n = input(texto)
	
	if n.isdecimal():
		print(f'Boa! {n} é um numero valido')
		
	else:
		print('Valor invalido')
		return LeiaInt(texto)
		
n = LeiaInt('Ola digite um numero')