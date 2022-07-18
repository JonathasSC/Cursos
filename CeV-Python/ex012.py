p = float(input("Digite o preço: "))
d = float(input("Digite o desconto em %: "))
r = p*d//100
print (f"{p} com desconto de {d}%\nfica {p-r} reais")
