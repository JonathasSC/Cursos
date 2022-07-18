resp = "S"
cont = soma = media = maior = menor = 0
while resp in "S":
	n = int(input("Digite um numero: "))
	soma += n
	cont += 1
	if cont == 1:
		maior = menor = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n
	resp = input("Quer continuar?[S/N]: ").upper().strip()
media = soma / cont
print(f"Voce digitou {cont} numeros e media entre eles é {media}")
print(f"o maior foi {maior} e o menor {menor}")