ficha = list()

while True:
	nome = str(input('Nome: '))
	nota1 = int(input('1° nota: '))
	nota2 = int(input('2° nota: '))
	media = (nota1 + nota2) // 2
	
	resp = input("desejar continuar?[S/N]").upper().strip()
	
	if resp == 'N':
		break
	else:
		pass

ficha.append([nome,[nota1,nota2],media])
print(ficha)

print(f'{ficha[0:0]}')