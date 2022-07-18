maiorpes = 0
menorpes = 0
for r in range(1,6):
    peso = float(input(f"Digite o peso da {r}°: Kg "))
    if r == 1:
        maiorpes = peso
        menorpes = peso
    else:
        if peso > maiorpes:
            maiorpes = peso
        if peso < menorpes:
            menorpes = peso
print(f"o menor peso foi {menorpes}kg e o maior foi {maiorpes}kg")

        
        
  