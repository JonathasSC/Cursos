import random 
bot = random.randint(0,10)
ganhos = 0
perdas = 0
print(f"{'Vamos jogar par ou impar!':^30}")
while perdas != 1:
	n = int(input("Digite um numero de 0 a 10: "))
	esc = input("escolha Par[ P ] ou impar[ I ]: ").upper().strip()
	soma = n + bot
	result = soma % 2
	if esc == "P":
		if result == 0:
			print("="*30)
			print(f"eu escolhi {bot}, então deu {soma}")
			print("VOCE GANHOU!")
			ganhos = ganhos + 1
			print("="*30)
			print(f"{'Vamos denovo!':^30}")
			print("="*30)
		else:
			print("="*30)
			print(f"eu escolhi {bot}, então deu {soma}")
			print("VOCE PERDEU :/")
			perdas = perdas + 1
			print("="*30)
	if esc == "I":
		if result == 1:
			print("="*30)
			print(f"eu escolhi {bot}, então deu {soma}")
			print("VOCE GANHOU!")
			ganhos = ganhos + 1
			print("="*30)
			print(f"{'Vamos denovo!':^30}")
			print("="*30)
		else:
			print("="*30)
			print(f"eu escolhi {bot}, então deu {soma}")
			print("VOCE PERDEU :/ ")
			perdas = perdas + 1
			print("="*30)
	if  perdas >= 1:
		break
if ganhos > 1 or ganhos == 0:
		print(f"Voce venceu {ganhos} vezes")
if ganhos == 1:
		print(f"Voce venceu {ganhos} vez")

