lista = []
resp = "S"

#sistema de repetição caso resp for "S"
while resp == "S":
	
	n = int(input("Digite um numero: "))
	#sistema de condição caso tiver "n" na lista
	if n in lista:
		print("Numero repetido, não irei salvar")
		
	else:
		print("Numero salvo..")
		lista.append(n)
	resp = input("Quer continuar?[S/N]: ").upper()

#mostrando resultado.
print (f"Sua lista em ordem ficou: \n{sorted(lista)}")