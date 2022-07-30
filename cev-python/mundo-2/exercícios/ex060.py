from math import factorial
n = int(input("Digite um número: "))
fac = factorial(n)
n2 = n + 1
print(f"o fatorial de {n} é o mesmo que:\n")
while n2 != 0:
    n2 = n2 - 1
    print(n2,"×",end=" ")
print(fac)