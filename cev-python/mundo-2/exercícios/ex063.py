termo = int(input("Quantos termos?: "))
t1 = 0
t2 = 1
cont = 3
print(f"{t1}→{t2}→",end=" ")
while cont <= termo:
    t3 = t1 + t2
    cont += 1
    print(f"{t3}→",end=" ")
    t1 = t2 
#t1 recebe t2 então t1 passa a ser o próximo número
    t2 = t3
#t2 recebe t3 então t2 passa a ser o próximo número
#assim:
    #2(t1) → 5(t2) → 7(t3)
    #5(t1) → 7(t3) → 12(t1+t2)(t3)
print("Fim")