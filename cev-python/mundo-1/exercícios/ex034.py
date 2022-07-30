#reajuste salarial 

salário = float(input("Digite o salário do funcionário:R$ "))
reajuste = float(input("De quantos % será o reajuste?: "))
print (f"O funcionário que ganhava R$ {salário}")
print(f"com reajuste de {reajuste} % passara a receber:")
print(f"R$ {(salário * reajuste / 100) + salário}")