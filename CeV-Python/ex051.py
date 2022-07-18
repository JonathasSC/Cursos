print("="*40)
print(f"{'10 PASSOS DE P.A':^40}")
print("="*40)
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite a razão: "))
decima = n1 + (10 - 1) * n2
for r in range(n1,decima,n2):
     print(f"{r} →",end=" ")
print ("Fim")