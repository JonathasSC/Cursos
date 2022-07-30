lista = []
resp = 'S'
while resp == "S":
	lista.append(int(input('Digite um valor: ')))
	resp = input('Quer continuar?[S/N]: ').upper()
print(f'Voce digitou {len(lista)} elementos')
print(f"Os valores em ordem decrescente ficaram {lista[::-1]}")
if 5 in lista:
	print('Contem o numero 5 na lista!')
else:
	print('Não contem o numero 5 na lista!')