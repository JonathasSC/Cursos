from datetime import date
ano = int(input("Em que ano você nasceu? "))
atual = date.today().year
idade = atual - ano 
if idade < 10:
    print("Você é considerado MIRIM")
elif idade > 9 and idade < 15:
    print("Você é considerado INFANTIL")
elif idade > 14 and idade < 19:
    print("Você é considerado JUNIOR")
elif idade > 18 and idade < 25:
    print ("Você é considerado SENIOR")
elif idade > 24:
    print("você é considerado MASTER")