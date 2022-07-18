#conversor de bases numéricas
n1 = int(input("Digite um número "))
print("Selecione uma das bases numéricas para converter")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
r = int(input("- "))
if r == 1:
    print(f"o número {n1} em binário é {bin(n1)[2:]}")
elif r == 2:
    print(f"o número {n1} em octal é {oct(n1)[2:1]}")
elif r == 3:
    print(f"o número {n1} em hexadecimal é {hex(n1)[2:1]}").split(0,1)