lista = {}

#função Notas:
def notas():
	
	#dados e notas
	nome_aluno = input('Nome do aluno: ')

	lista['1° nota:'] = float(input('Digite a 1° nota: '))
	
	lista['2° nota:'] = float(input('Digite a 2° nota: '))
		
	lista['3° nota:'] = float(input('Digite a 3° nota: '))
	
	
	#calculo da media
	nota_final = 0 
	for s in lista.values():
		nota_final = nota_final + s
	nota_final = nota_final//3
	
	#mostrar nome do aluno
	print(f'Nome: {nome_aluno}')
	
	#mostrar chaves e valores das notas
	for k,v in lista.items():
		print(k,v)
		
	print('media:  ',nota_final)
	
	if nota_final < 6.0:
		print('Reprovado')
	else:
		print('Aprovado')
	print('-'*25)	
		
#loop 
while True:
	notas()