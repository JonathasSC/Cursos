sexo = input("Por favor informe seu sexo [M/F]: ").upper().strip()
while sexo != "M" and sexo != "F":
    sexo = input("opção de sexo inválido, digite novamente: ").upper().strip
if sexo == "F":
    sexo = "feminino"
    print(f"Certo, seu sexo é {sexo}")
if sexo == "M":
    sexo = "masculino"
    print(f"Certo, seu sexo é {sexo}")