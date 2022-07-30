from datetime import date
ano = date.today().year

def votação(ano_nasci):
	idade = ano - ano_nasci
	
	if idade > 17 and idade < 65:
		print(f'Com {idade} anos: Seu voto é obrigatorio.')
		
	if idade < 17:
		print(f'Com {idade} anos: não vota.')
	
	if idade == 17 or idade > 65:
		print(f'Com {idade} anos: seu voto é opcional.')
		
ano_nasci = int(input('Em que ano voce nasceu?: '))

votação(ano_nasci)