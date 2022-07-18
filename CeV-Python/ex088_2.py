from random import sample
from time import sleep

nums = range(0,61)
jogos = []
cont = 0
linha = "="*30

print(linha)
print(f"{'Bem vindo':^28}")

print(linha)
n_jogos = int(input("Quantos palpites quer fazer?: "))
print(linha)

cont = 0

print("gerando palpites...")
print()
sleep(2)

while True:
	cont += 1
	for q in range (0,6):
		jogos = sample(nums,6)
			
	print(sorted(jogos))
	if cont < n_jogos:
		pass
	else:
		break
	del jogos [:]


print()
print(linha)
print("Boa sorte!")