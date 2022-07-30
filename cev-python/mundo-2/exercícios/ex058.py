from random import randint
tentativa = 0
comput = randint(0,10)
frase = "Olá, eu sou seu computador\nEu pensei em um número de 0 a 10...\ntente adivinhar qual número pensei!"
print(frase)
palpite = int(input("O computador pensou em: "))
while palpite != comput:
    palpite = int(input("Errou! , eu pensei em outro número\ntente novamente: "))
    tentativa = tentativa + 1
tentativa = tentativa + 1
if tentativa > 5:
    print(f"Vixe, Você precisou de {tentativa} tentativas")
if tentativa < 5:
    print(f"Boa! você so precisou de {tentativa} tentativas")