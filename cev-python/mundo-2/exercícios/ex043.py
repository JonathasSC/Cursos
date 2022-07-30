kg = float(input("Qual é sua massa em Quilos: "))
m = float(input("Qual é a sua altura em Metros: "))
IMC = kg / (m**2)
print(f"Seu Índice de massa corporal é {IMC:.2f}")
if IMC < 18.5:
    print("você está abaixo da massa ideal")
elif IMC >= 18.5 and IMC <= 25:
    print("Você está com massa ideal")
elif IMC >= 25 and IMC <= 30:
    print("você está com sobrepeso, fique atento!")
elif IMC >= 30 and IMC <= 40:
    print("você está com obesidade, SE CUIDE!")
elif IMC >= 40:
    print("você está com obesidade morbida, CUIDADO!")