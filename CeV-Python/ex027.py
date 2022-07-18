#primeiro e última nome

nome = input ("diga seu nome: ").strip().split()
print(f"seu primeiro nome é {nome[0].title()}")
nome1 = nome[len(nome)-1]
print(f"seu último nome é {nome1.title()}")