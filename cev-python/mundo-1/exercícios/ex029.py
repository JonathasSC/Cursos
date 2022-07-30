velocidade = float(input("Qual a velocidade do carro?: "))
if velocidade > 60:
    acima = velocidade - 60
    preço = acima * 7
    print("MULTADO! sua velocidade passou de 60km/h")
    print(f"Sua conta é R${preço}")
else :
    print("TUDO CERTO!, tenha uma boa viagem")