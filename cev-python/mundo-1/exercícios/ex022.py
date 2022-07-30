from time import sleep
nome = input ("Digite seu nome: ")

print(nome.upper())

print(nome.lower())

nome2 = nome.split()

nome3 = ''.join(nome2)

print(f"{nome} tem {len(nome3)} letras")
print(f"e {nome2[0]} tem {len(nome2[0])}")

