#em = float(input("Qual o valor do empréstimo: R$ "))
#s = float(input ("De quanto é o seu salário?: R$ "))
#p = float(input ("Quantas prestações você pretende pagar? "))
#if em / p < s * 2:
#    print(f"O empréstimo de {em} fica\nR$ {em / p:.2f} em {p:.0f} prestações")
#    print("EMPRÉSTIMO ACEITO")
#else:
#    print(f"O empréstimo de {em} fica\nR$ {em / p:.2f} em {p:.0f} prestações")
#    print("EMPRESTIMO NEGADO")

casa = float(input("Qual o valor da casa? R$ "))
salário = float(input ("Qual o salário do comprador? R$ "))
finança = float(input("Quantos anos de financiamento? "))
parcela = casa / (finança * 12)
porc = salário * 30 / 100
print (f"{finança} anos de finança de R${casa} ficará R${parcela:.2f}")
if porc >= parcela :
     print("FINANCEAMENTO APROVADO")
else:
     print("FINANCIAMENTO NEGADO")