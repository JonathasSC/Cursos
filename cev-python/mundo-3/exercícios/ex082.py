lstp = []
lsti = []
print("Digite -1 para parar")
while True:
	n = int(input("Digite um numero: "))
	if n == -1:
		break
	resu = n % 2
	if resu == 0:
		lstp.append(n)
	if resu == 1:
		lsti.append(n)
print("="*35)
print(f"voce digitou\n{lsti+lstp}")
print("="*35)
print(f"{lsti} são impar")
print("="*35)
print(f"{lstp} são par")