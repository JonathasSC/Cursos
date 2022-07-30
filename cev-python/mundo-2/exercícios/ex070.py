mbarato = 0
nmbarato = " "
contk = 0
cont = 0
soma = 0
print("-"*30)
print(f"{'LOJA DO AWAYZ':^30}")
print("-"*30)
resp = "S"

while resp == "S" and resp != "N":
	produto = input("nome do produto: ")
	preço = float(input("preço: R$ "))
	soma = preço + soma
	print("-"*30)
	resp = input("Quer continuar? [ S/N ]: ").upper().strip()
	print("-"*30)
	cont = cont + 1
	
	if cont == 1:
		mbarato = preço
		nmbarato = produto
	if cont > 1:
		if preço < mbarato:
			mbarato = preço
			nmbarato = produto
	if preço > 1000:
		contk = contk + 1
print(f"O total deu : R$ {soma}")
print(f"{contk} produtos acima de R$ 1000")
print(f"O mais barato é {nmbarato} custando R${mbarato:.2f}")