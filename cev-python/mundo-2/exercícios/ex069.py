cont = 0
mcad = 0
cont18 = 0
mn18 = 0
resp = "S"
while resp != "N" and resp == "S":
	sexo = input("Digite o sexo [ M / F ]: ").strip().upper()
	idade = int(input("Digite a idade: "))
	print("="*30)
	resp = input("Quer continuar?[ S / N ]: ").strip().upper()
	print("="*30)
	if idade < 18:
		cont18 = cont18 + 1
	if sexo == "M":
		mcad = mcad + 1
	if sexo == "F" and idade < 20:
		mn18 = mn18 + 1
print(f"{mn18} mulheres tem menos de 20 anos ")
print(f"{cont18} pessoas tem menos de 18")
print(f"{mcad} foram homens")