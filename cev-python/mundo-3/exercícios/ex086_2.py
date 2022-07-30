from random import sample

def Linha():
	print("_"*31,"\n")
	return Linha

Linha()
print(f"{'BEM VINDO AO SORTEADOR':^30}")
Linha()

np = int(input('Quantos palpites voce quer? '))

resp = "S"

while resp == "S":
	for n in range(0,np):
		result = sample(range(0,61),6)
		print(f"{n+1}° jogo: {sorted(result)}")
	
	Linha()
	resp = input("Deseja sortear novos jogos? [S/N]: ").upper().strip()
	Linha()

print(f"{'PROGRAMA ENCERRADO':^30}")
Linha()	