import androidhelper
from time import sleep
droid = androidhelper.Android()
droid.ttsSpeak("Bem vindo à Loja do Jonathas")
droid.ttsSpeak("quanto deu a sua compra?")
print(f"{'LOJA DO JONATHAS':=^40}")
preço = float(input("Preço das compras: R$"))
droid.ttsSpeak("digite a forma de pagamento")
print("\nFORMAS DE PAGAMENTO:")
print("[ 1 ] á vista dinheiro/cheque")
print("[ 2 ] cartão de crédito")
print("[ 3 ] cartão de débito")
fp = int(input ("Qual a opção: "))
if fp == 1:
    desc = (preço*15)/100
    print(f"Sua compra de R${preço} ficará R${preço-desc}")
elif fp == 2:
    parce = int(input("Quantas vezes pretende parcelar? "))
    if parce == 1: 
       desc = (preço*5)/100
       print(f"Sua compra de R${preço}\nficará {parce}X de {preço-desc} com desconto")
    if parce == 2:
       print(f"Sua compra de R${preço}\nficará {parce}X de R${preço/parce} sem juros")
    if parce > 2:
       juros = preço*20/100
       print(f"Sua compra de R${preço}\nficará {parce}X de R${(preço+juros)/parce} com juros")
elif fp == 3:
    juros = preço*10/100
    print(f"Sua compra de R${preço}\nficará R${preço+juros} com juros")
else:
    print(f"Opção de pagamento inválida!\n{'TENTE NOVAMENTE':-^25}")