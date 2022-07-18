def notas(sit=True):
	def line():
		print('-'*20)
	
	r = dict()
	dados = dict()

	nome = input('nome do aluno: ')
	
	dados['nota 1: '] = int(input('nota 1: '))
	dados['nota 2: '] = int(input('nota 2: '))
	dados['nota 3: '] = int(input('nota 3: '))
	
	line()
	
	r['maior nota: '] = max(dados.values())
	r['menor nota: '] = min(dados.values())
	r['media: '] = 0
	
	for s in dados.values():
		r['media: '] = r['media: '] + s
	r['media: '] = r['media: ']/len(dados)
		

	if sit:
 		
		if r['media: '] >= 6:
			r['situação: '] = 'BOA'	
		elif r['media: '] <= 5:
			r['situação: '] = 'RUIM'
 			
	for k,v in r.items():
		print(k,v)

	line()
	
while True:
	notas()
	
