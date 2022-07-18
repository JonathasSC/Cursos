print("="*30)
print(f"{'BANCO AWZ':^30}")
print("="*30)
valor = float(input("Quanto você quer sacar?: R$"))
total = valor
nome = ""
totalced = 0
ced = 200
while True:
	if total >= ced:
		total -= ced
		totalced += 1
	else:
		print(f"total de {totalced} cedulas de R$ {ced}")
		if ced == 200:
				ced = 100
		elif ced == 100:
			ced = 50
		elif ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		totalced = 0
		if total == 0:
			break