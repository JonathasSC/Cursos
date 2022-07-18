cont = 0
n = 0
soma = 0
while n != 999:
    n = n + n
    n = int(input("Digite um número [999 = para]: "))  
    cont = cont + 1  
    soma = soma + n 
print(f"Você digitou {cont-1} números e a soma deu {soma-999}")