print ("=-"*20)
nome = "FORMANDO TRIÂNGULOS"
print (f"{nome:>29}")
print("-="*20)
n1 = float(input("Tamanho do 1° segmento: "))
n2 = float(input("Tamanho do 2° segmento: "))
n3 = float(input("Tamanho do 3° segmento: "))
print("--"*20)
if n3 > n1+n2 and n1 > n2+n3 or n2 > n3+n1:
    print("Os segmentos FORMAM um triângulo")
else:
    print ("Os segmentos NÃO formam um triângulo")