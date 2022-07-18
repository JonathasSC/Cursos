n = int(input("Digite um número: "))
cont = 0
for r in range(1,n+1):
    if n % r == 0:
        cont = cont + 1
if cont > 2 :
   print("ESSE NÚMERO NÃO É PRIMO")
else:
   print("ESSE NÚMERO É PRIMO")