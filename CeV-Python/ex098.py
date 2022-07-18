from time import sleep 

def Linhas():
	print('='*35)


print('Uma contagem de 1 a 10 de 1 em 1')
n = 10
while n != 1:
	
	if n == 10:
		print(n,end=' ')
	else:
		pass
	n = n - 1
	print(n,end=' ')
print('\n')
Linhas()

print('Uma contagem de 10 ate 0 de 2 em 2')
n = 10
while n != 0:
	if n == 10:
		print(n,end=' ')
	n = n - 2
	print(n,end=' ')
print('\n')
Linhas()


inicio = int(input('Digite um numero: '))
chegada = int(input('Numero final: '))
pulos = int(input('De quanto em quanto?: '))

if inicio < chegada:
	while inicio != chegada:
		inicio = inicio + pulos
		print(inicio)
		
if inicio > chegada:
	while inicio != chegada:
		inicio = inicio - pulos
		print(inicio)
		
	