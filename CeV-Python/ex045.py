from random import randint
from time import sleep
print("="*40)
print(f"{'VAMOS JOGAR JO KEN PO':^40}")
print("="*40)
print("ESCOLHA UMA ALTERNATIVA")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
print("="*40)
itens = ("pedra","papel","tesoura")
bot = randint(0,2)
resp = int(input("Qual é a sua escolha? "))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.5)
print("-"*40)
if resp == bot:
    print(f"EMPATE! eu também escolhi {(itens[bot])}")
elif resp == 0 and bot != 1:
    print(f"VOCÊ VENCEU eu joguei {(itens[bot])}")
elif resp == 1 and bot != 2:
    print(f"VOCÊ VENCEU eu escolhi {(itens[bot])}")
elif resp == 2 and bot != 0:
    print(f"VOCÊ VENCEU eu escolhi {(itens[bot])}")
elif resp == 0 and bot == 1:
    print(f"EU GANHEI!, eu escolhi {(itens[bot])}")
elif resp == 1 and bot == 2:
    print(f"EU GANHEI!, eu escolhi {(itens[bot])}")
elif resp == 2 and bot == 0:
    print(f"EU GANHEI, eu escolhi {(itens[bot])}")
elif resp != 0 and resp != 1 and resp != 2:
    print(f"JOGO CANCELADO, escolha um número válido")