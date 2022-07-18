#sem importação
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
print (f"O comprimento da hipotenusa é {(ca**2+co**2)**(1/2):.3f}")

import math 
print (f"O comprimento da hipotenusa é {math.hypot(co,ca):.3f}")