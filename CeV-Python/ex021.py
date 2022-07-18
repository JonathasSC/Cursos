import playsound
import androidhelper
from time import sleep
droid = androidhelper.Android()
droid.ttsSpeak("Bem vindo ao player de música")
sleep(0.3)
droid.ttsSpeak("Qual música você quer ouvir?")
sleep(0.3) 
droid.ttsSpeak("Selecione uma das músicas da lista")
sleep(0.5)
lista = "LISTA DE MÚSICA"
print("="*40)
print(f"{lista:>27}")
print("-"*40)
print ("1 - Nirvana - Smell like teen spirit\n")
print ("="*40)
music = int(input("qual música você quer ouvir?: "))
if music == 1:
    playsound.playsound('Nirvana.mp3')
