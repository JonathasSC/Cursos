print("="*35)
print(f"{'PROGRESSÃO ARITMÉTICA':^35}")
print("="*35)
n = int(input("Digite um número: "))
r = int(input("Digite a razão: "))
termo = n 
cont = 1
total = 0
mais = 10
while mais != 0: 
    total = total + mais
    while cont <= total:        
        print(f"{termo}->",end=" ")
        termo += r 
        cont = cont + 1        	    
    print("PAUSA!")
    mais = int(input("quantos termos você ver quer a mais?: "))
print(f"foi lhe mostrado um total de {cont-1} termos")
print("FIM")