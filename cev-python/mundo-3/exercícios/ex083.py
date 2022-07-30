exp = input("digite uma expressão: ")
pilha = []
for simb in exp:
	if simb == '(':
		pilha.append(')')
	elif simb == ')':
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')
			break
if len(pilha) == 0:
	print("sua expressão é VALIDA")
else:
	print("sua expressão é INVALIDA")