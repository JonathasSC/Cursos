pv = float(input("Digite o primeiro valor: "))
sv = float(input("Digite o segundo valor: "))
print("[1] Somar")
print("[2] multiplicar")
print("[3] qual o maior?")
print("[4] novos números")
print("[0] sair do programa")
op = int(input("> Qual opção você deseja?: "))
while op != 0:
    if op == 1:
        print(f"{pv:.0f} + {sv:.0f} = {pv+sv:.0f}")
    if op == 2:
        print(f"{pv:.0f} × {sv:.0f} = {pv*sv:.0f}")
    if op == 3:
        if pv > sv:
            print(f"{pv} é o maior")
        if pv < sv:
            print(f"{sv} é o maior")
    if op == 4:
        pv = float(input("Digite o primeiro valor: "))
        sv = float(input("Digite o segundo valor: "))
    print("="*30)
    print("[1] Somar")
    print("[2] subtrair")
    print("[3] qual o maior?")
    print("[4] novos número")
    print("[0] sair do programa")
    op = int(input("> Qual opção você deseja?: "))
print("="*30)
print(f"programa encerrado!")