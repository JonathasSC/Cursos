print("Bem vindo ao analisador de triângulos")
l1 = float(input("Qual o valor do primeiro lado? "))
l2 = float(input("Qual o valor do segundo lado? "))
l3 = float(input("Qual o valor do terceiro lado? "))
if l1 != 0 and l2 != 0 and l3 != 0:
    if l1 == l2 and l2 == l3:
        print("O triângulo é considerado EQUILÁTERO")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("O triângulo é considerado ISOSCELES")
    elif l1 < l2 and l1 < l3:
        print("O triângulo é considerado ACUTÂNGULO")
    elif l2 < l1 and l2 < l3:
        print("O triângulo é consideração ACUTÂNGULO")
    elif l3 < l1 and l3 < l2:
        print("O triângulo é considerado ACUTÂNGULO")
else:
    print("O VALOR 0 É INVALIDO")