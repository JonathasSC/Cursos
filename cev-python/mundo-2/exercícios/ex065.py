lista = []
cont = 0

while True:
	n = int(input("Digite um numero: "))
	lista.append(n)
	r = input("Quer continuar?[S/N]: ").upper().strip()
	cont = cont + 1
	if r == "N":
		break
	else:
		pass
		
print(f"A media foi {sum(lista)/cont:.2f}")

print(f"O maior numero foi {max(lista)} e o menor foi {min(lista)}")