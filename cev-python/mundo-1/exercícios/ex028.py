import random
import androidhelper
droid = androidhelper.Android()
droid.ttsSpeak("Bem vindo ao jogo de adivinhações")
droid.ttsSpeak("Vou pensar em um número de 0 a 5")
print("=-"*20)
print("Vou pensar em um número entre 0 e 5")
print("=-"*20)
droid.ttsSpeak("Qual Número estou pensando?")
n = int(input("qual número estou pensando: "))
lista = [1,2,3,4,5]
aleatório = random.choice(lista)
if n == aleatório:
    print(f"Ganhou!, eu estava pensando no {n}")
else:
    print(f"Perdeu!, eu estava pensando no {aleatório}")
