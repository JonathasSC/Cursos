aluno = {'Aluno':'','Media':''}
aluno['Aluno']= input('Aluno: ')
aluno['Media'] = float(input('Media: '))
print('='*35)
#print(f"{aluno.keys[0]} é {aluno['Nome']}")
for k,v in aluno.items():
	print(f"{k} é {v}")