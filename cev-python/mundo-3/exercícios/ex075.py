lista = [ ]
pares = [ ]
for n in range (0,5):
	lista.append(int(input("Digite um numero: ")))
print(f"O numero 9 apareceu {lista.count(9)} vez(es) na lista\n","="*35)
if 3 in lista:
	print(f"O numero 3 esta na posição {lista.index(3)+1}\n","="*35)
else:
	print("Não houve o numero 3 na lista\n","="*35)
for l in lista:
	if l % 2 == 0:
		pares.append(l)
print(f"Teve {len(pares)} numeros pares na lista\n{pares}")