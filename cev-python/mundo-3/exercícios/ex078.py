lista = []
menor = maior = 0

for r in range (0,6):
	lista.append(int(input(f"Digite um valor na {r}° posição: ")))
	
	if r == 0:
		menor = lista[r]
		maior = lista[r]
	else:
		if lista[r] < menor:
			menor = lista[r]
		if lista[r] > maior:
			maior = lista[r]
			
print(f"Voce digitou {lista}")

print(f"o menor valor foi {menor} na posição ",end="")
for i, v in enumerate(lista):
	if menor == v:
		print(i)
		
print(f"o maior valor foi {maior} na posição ",end="")
for i, v in enumerate(lista):
	if maior == v:
		print(i)