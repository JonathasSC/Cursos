s = float(input("Qual o salário do funcionário: "))
r = float(input("quanto foi o reajuste salarial: "))
print (f"O funcionário com salário de {s}\nreais com o reajuste de {r}%")
print (f"tem agora um salário de {(s*r/100)+s} reais")