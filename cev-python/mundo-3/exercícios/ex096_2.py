msg = "Controle de Terreno"
tam = len(msg)+4

def Escreva (msg,tam):
	print("-"*tam)
	print(f"  {msg}")
	print("-"*tam)


def area():
	
	print(f"\nA area desse terreno é:")
	print(l*c,'m2')


#principal code
Escreva(msg,tam)
l = float(input("Digite a largura(m): "))
c = float(input("Digite o comprimento(m): "))

area()
print("-"*tam)