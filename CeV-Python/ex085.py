pares = []
impares = []

for v in range(0,7):
	num = int(input(f"Digite o {v+1}° numero: "))
	result = num % 2 
	if result == 0:
		pares.append(num)
	else:
		impares.append(num)
		
print("="*35)
print(f"Os numeros pares foram {sorted(pares)}")
print(f"Os numeros impares foram {sorted(impares)}")