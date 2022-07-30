n = 0
import random
r = random.randint(0,10)
n = " "
print("Vamos jogar Par ou Impar!")
print("Quando quiser parar digite '11'")
while n != 11:
	print("="*30)
	n = int(input("Digite um numero: "))
	e = input("Par ou impar?[P/I]: ").strip().upper()
	soma = r + n 
	if e == "P":
		result = soma % 2
		if result == 0:
			print(f"Eu coloquei {r} então deu {soma}")
			print("VOCE GANHOU!")
		else:
			print(f"Eu coloquei {r} então deu {soma}")
			print("VOCE PERDEU!")
			print("="*30)
	if e == "I":
		result = soma % 2
		if result == 1:
			print(f"Eu coloquei {r} então deu {soma}")
			print("VOCE GANHOU!")
		else:
			print(f"Eu coloquei {r} então deu {soma}")
			print("VOCE PERDEU!")
		print("="*30)
	print(f"{'Vamos continuar!':^30}")