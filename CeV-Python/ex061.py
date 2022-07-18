print("="*35)
print(f"{'10 TERMOS DE UMA P.A':^35}")
print("="*35)
n = int(input("Digite um número: "))
r = int(input("Digite a razão: "))
deci = n + ( 10 - 1 ) * r 
print(f"{n} ->",end=" ")
while n != deci:
    n = n + r 
    print(f"{n} ->",end=" ")
print("fim")