from datetime import date
ano = int(input("Em que ano você nasceu?: "))
atual = date.today().year
anos = atual - ano
print(f"você tem {anos} anos")
if anos == 18:
    print("VOCÊ DEVE SE ALISTAR")
elif anos > 18:
    print("VOCÊ DEVERIA TER SE ALISTADO")
    print(f"o alistamento deveria ser feito em {ano+18}")
else:
    print("VOCÊ NÃO PODE SE ALISTAR ATUALMENTE")
    print(f"você podera se alistar em {ano+18}")
    