from math import factorial
def fatorial(n):
	
	for c in range(n,0,-1):
		print(c,end='')
		if c > 1:
			print (' × ',end='')
		else:
			print(' = ',end='')
			
	print(factorial(n))
n = int(input('Digite um numero: '))
fatorial(n)		