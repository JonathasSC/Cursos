soma = 0
cont = 0
for q in range(1,7):
    num = int(input(f"Digite o {q}° valor "))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print(f"Dos números que você informou {cont} são pares e a soma deles é {soma}")