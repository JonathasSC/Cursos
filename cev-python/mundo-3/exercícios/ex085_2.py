num = [[],[]]
valor = 0

for c in range(1,8):
	valor = int(input(f"Digite o {c}° valor: "))
	if valor % 2 == 0:
		num[0].append(valor)
	else:
		num[1].append(valor)
		
print("="*35)
print(f"Os numeros pares foram {sorted(num[0])}")
print(f"Os numeros impares foram {sorted(num[1])}")