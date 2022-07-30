c = soma = 0
while True:
	n = int(input("Digite um numero ou 999 para parar: "))
	if n == 999:
		break
	soma += n
	c += 1
print("Voce digitou",c,"numeros")
print("A soma deles é",soma)