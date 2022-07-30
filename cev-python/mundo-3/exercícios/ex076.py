print(f"{'LISTAGEM DE PREÇO':^38}")
print("="*37)
listagem = ('Arroz',7.99,
'Feijão',9.49,
'Macarrão',4.59,
'Achocolatado',8.49,
'Biscoito',1.25,
'Bolacha',2.99)
for pos in range(0,len(listagem)):
	if pos % 2 == 0:
		print(f"{listagem[pos]:.<30}",end="")
	else:
		print(f"R$ {listagem[pos]:>2.2f}")
print("="*37)		