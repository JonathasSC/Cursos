import datetime
date = datetime.date.today()
year = date.strftime("%Y")

dados = {'nome':'','nasci':0,'cart':0,'contrat':0,'salario':0}

dados['nome'] = input('Digite o nome: ')
dados['nasci'] = input('Digite o ano de nascimento: ')
dados['cart'] = input('Carteira de trabalho ( 0 não tem ): ')

data_nascimento = dados['nasci']

idade = year - data_nascimento
print(idade)

if dados['cart'] != 0:
	dados['contrat'] = input('Ano de contratação: ')
	dados['salario'] = input('Salario mensal: ')
	
	print(f"	- nome: {dados['nome']}")
	print(f"	- idade: ")
	print
#else:
	