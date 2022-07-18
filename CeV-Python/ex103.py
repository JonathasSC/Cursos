try:
	nome = input('Nome do jogador: ')
except:
	nome = '<desconhecido>'
	
if nome == '' or nome.isnumeric() == True:
	nome = '<desconhecido>'
	
try:
	gols = int(input('Numero de gols: '))
except:
	gols = 0
	
print(f'O jogador {nome} fez {gols} gols')