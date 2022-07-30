msg = input("Digite algo: ")

def Escreva (msg):
	tam = len(msg) + 4
	print("="*tam)
	print(f"  {msg}")
	print("="*tam)

Escreva(msg)