str = input("Digite algo: ")
if str.isnumeric() == True:
	print(f"{str} é um numero")
else:
	print(f"{str} NÃO é um numero")
if str.isalpha() == True:
	print(f"{str} é alfabetico")
else:
	print(f"{str} NÃO é alfabetico")
if str.isalnum() == True:
	print(f"{str} é alfanumerico")
else:
	print(f"{str} NÃO é alfanumerico")
if str.isdigit() == True:
	print(f"{str} é um digito")
else:
	print(f"{str} NÃO é um digito")
if str.isupper() == True:
	print(f"{str} é totalmente em caixa alta")
else:
	print(f"{str} NÃO esta totalmente em caixa alta")