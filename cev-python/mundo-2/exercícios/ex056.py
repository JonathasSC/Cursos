somaidade = 0
maioridade = 0
nomevelho = ' '
maioridadeH = 0
mulhernova = 0
for pessoas in range (1,5):
    print(f"-----{pessoas}° Pessoa-----")
    nome = input("Digite seu nome: ").strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Diga seu sexo [M/F]: ")).upper().strip()
    somaidade = somaidade + idade
    mediaidade = somaidade / 4
    if pessoas == 1 and sexo == "M":
        maioridadeH = idade
        nomevelho = nome
    if sexo == "M" and idade > maioridadeH:
        maioridadeH = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulhernova = mulhernova + 1
print(f"A média entre as idades é {mediaidade:.2f} anos")
print(f"O Homem mais velho tem {maioridadeH} e seu nome é {nomevelho}")
print(f"Temos {mulhernova} mulheres com menos de 20")