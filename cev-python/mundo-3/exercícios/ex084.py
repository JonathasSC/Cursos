tempData = []
eternData = []
maior = menor = 0
resp = "S"

while True:
	tempData.append(str(input("Nome: ")))
	tempData.append(str(input("Peso: ")))
	if len(eternData) == 0:
		maior = menor = tempData[1]
	else:
		if tempData[1] > maior:
			maior = tempData[1]
		if tempData[1] < menor:
			menor = tempData[1]
	eternData.append(tempData[:])
	tempData.clear()
	resp = input("Quer continuar [S/N]: ").upper()
	while resp != "N" and resp != "S":
		resp = input("Voce digitou uma opção invalida, escolha entre [S/N]: ").upper()
	if resp == "N":
		break
		
		
print(f"Voce cadastrou {len(eternData)} pessoas")
print(f"O maior peso foi {maior}kg de ",end="")
for p in eternData:
	if p[1] == maior:
		print(f"{p[0]}")
print(f"O menor peso foi {menor}kg de ",end="")
for p in eternData:
	if p[1] == menor:
		print(f"{p[0]}")