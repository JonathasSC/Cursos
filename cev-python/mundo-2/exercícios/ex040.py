n1 = float(input("digite a primeira nota "))
n2 = float(input("digite a segunda nota "))
media = (n1+n2)/2
if media < 6:
    print(f"a média do aluno é {media:.2f}")
    print("ALUNO REPROVADO")
else:
    print(f"a média do aluno é {media:.2f}")
    print("ALUNO APROVADO")
