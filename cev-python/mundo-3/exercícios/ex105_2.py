def notas(*n, sit=False):
 	r = dict()
 
 	r['total'] = len(n)
 	r['maior'] = max(n)
 	r['menor'] = min(n)
 	r['media'] = sum(n)//len(n)
 	
 	if sit:
 		
 		if r['media'] >= 6:
 			r['situação'] = 'BOA'
 			
 		if r['media'] <= 5:
 			r['situação'] = 'RUIM'
 			
 	return r

resp = notas(3,4,5,sit=True)
print(resp)