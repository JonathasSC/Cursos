n = 0
while True:
	print("="*30)
	n = int(input("Digite um numero: "))
	if n < 0:
		break
	for t in range(1,11):
		print(f"{n} × {t} = {n*t}")
print("Programa encerrado")