def area(larg,comp):
	a = larg*comp 
	print(f'Um terreno {larg}×{comp} tem area {a}m²')
	
	
l = float(input('Largura: '))
c = float(input('Comprimento: '))

area(l,c)